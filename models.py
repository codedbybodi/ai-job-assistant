from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from db import Base 

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False, index=True)
    password_hash = Column(String, nullable=False)
    created_at = Column(DateTime, default=func.now())
    applications = relationship("Application", back_populates="user")

class Application(Base):
    __tablename__ = "applications"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    company_url = Column(String)
    job_description = Column(Text)
    cv_summary = Column(Text)
    cover_letter = Column(Text)
    interview_tips = Column(Text)
    created_at = Column(DateTime, default=func.now())
    user = relationship("User", back_populates="applications")
 