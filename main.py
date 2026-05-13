from fastapi import FastAPI, Depends, HTTPException, BackgroundTasks
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from typing import List
from db import get_db, engine
from auth import hash_password, verify_password, create_access_token, decode_token
from services.ai import analyze_job
from services.scraper import scrape_company
import schemas, models

models.Base.metadata.create_all(bind=engine)
app = FastAPI(title="AI Job Application Assistant", version="2.0.0")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

# AUTH DEPENDENCY
def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    try: 
        email = decode_token(token)
    except ValueError:
        raise HTTPException(status_code=401, detail="Invalid token")
    user = db.query(models.User).filter(models.User.email == email).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# AUTH ROUTES
@app.post("/register", tags=["Auth"])
def register(data: schemas.RegisterInput, db: Session = Depends(get_db)):
    if db.query(models.User).filter(models.User.email == data.email).first():
        raise HTTPException(status_code=400, detail="Email already registered")
    user = models.User(
        name=data.name,
        email=data.email,
        password_hash=hash_password(data.password)
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return {"message": "Registered!", "user_id": user.id}

@app.post("/login", tags=["Auth"])
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == form_data.username).first()
    if not user or not verify_password(form_data.password, user.password_hash):
        raise HTTPException(status_code=401, detail="Wrong credentials")
    return {"access_token": create_access_token({"sub": user.email}), "token_type": "bearer"}

@app.get("/me", tags=["Auth"])
def get_me(current_user: models.User = Depends(get_current_user)):
    return {"id": current_user.id, "name": current_user.name, "email": current_user.email}

# APPLICATION ROUTES
@app.post("/applications", response_model=schemas.ApplicationResponse, tags=["Applications"])
def create_application(data: schemas.ApplicationCreate, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    # Step 1 - Scrape Company Info
    company_info = scrape_company(data.company_url)
    # Step 2 - AI Analysis
    result = analyze_job(company_info, data.job_description, current_user.name)

    # Step 3 - Save to DB
    app_record = models.Application(
        user_id=current_user.id,
        company_url=data.company_url,
        job_description=data.job_description,
        cover_letter=result["cover_letter"],
        interview_tips=result["interview_tips"]
    )
    db.add(app_record)
    db.commit()
    db.refresh(app_record)
    return app_record

@app.get("/applications", response_model=List[schemas.ApplicationCreate], tags=["Applications"])
def get_applications(db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    return db.query(models.Application).filter(models.Application.user_id == current_user.id).order_by(models.Application.created_at.desc()).all()

@app.get("/applications/{id}", response_model=schemas.ApplicationCreate, tags=["Applications"])
def get_application(id: int, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    app_record = db.query(models.Application).filter(models.Application.id == id, models.Application.user_id == current_user.id).first()
    if not app_record:
        raise HTTPException(status_code=404, detail="Application not found")
    return app_record


@app.delete("/applications/{id}", tags=["Applications"])
def delete_application(id: int, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    app_record = db.query(models.Application).filter(models.Application.id == id, models.Application.user_id == current_user.id).first()
    if not app_record:
        raise HTTPException(status_code=404, detail="Not found")
    db.delete(app_record)
    db.commit()
    return { "message": "Deleted!"}
