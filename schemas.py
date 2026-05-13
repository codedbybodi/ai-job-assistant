from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class RegisterInput(BaseModel):
    name: str
    email: str
    password: str

class ApplicationCreate(BaseModel):
    company_url: str
    job_description: str

class ApplicationResponse(BaseModel):
    id: int
    company_url: str
    job_description: str
    cv_summary: Optional[str]
    cover_letter: Optional[str]
    interview_tips: Optional[str]
    created_at: datetime
    
    class Config:
        from_attributes = True

        