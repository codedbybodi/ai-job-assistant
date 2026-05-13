from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext
from dotenv import load_dotenv
import os

load_dotenv()

SECRET_KEY = os.environ.get("SECRET_KEY", "your-secret-key-here")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Hash a password before saving to DB
def hash_password(password: str) -> str:
    # bcrypt supports up to 72 bytes
    if len(password.encode("utf-8")) > 72:
        raise ValueError("Password too long. Maximum is 72 bytes")
    return pwd_context.hash(password)

# Check if a plain password matches the hashed on
def verify_password(plain: str, hashed: str) -> bool:
    return pwd_context.verify(plain, hashed)

# Create a JWT token for a user
def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

# Decode a token and get the user's email
def decode_token(token: str) -> str:
    try: 
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email = payload.get("sub")
        if email is None:
            raise ValueError("Invalid token")
        return email
    except JWTError:
        raise ValueError("Invalid or expired token")
