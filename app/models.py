from sqlalchemy import Column, Integer, String, Text, Date, DateTime, Boolean
from datetime import datetime
from app.database import Base

class Education(Base):
    __tablename__ = "education"
    
    id = Column(Integer, primary_key=True, index=True)
    school_name = Column(String(200), nullable=False)
    degree = Column(String(200), nullable=False)
    year = Column(String(50), nullable=False)
    achievements = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)

class Skill(Base):
    __tablename__ = "skills"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    category = Column(String(50), nullable=False)  # "technical" or "soft"
    level = Column(String(20), nullable=False)  # "basic", "intermediate", "advanced"
    description = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)

class Project(Base):
    __tablename__ = "projects"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=False)
    technologies = Column(String(300), nullable=False)
    github_link = Column(String(300))
    demo_link = Column(String(300))
    image_url = Column(String(300))
    created_at = Column(DateTime, default=datetime.utcnow)

class Experience(Base):
    __tablename__ = "experience"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    company = Column(String(200))
    location = Column(String(100))
    start_date = Column(String(50))
    end_date = Column(String(50))
    description = Column(Text)
    type = Column(String(50))  # "internship", "job", "volunteer"
    created_at = Column(DateTime, default=datetime.utcnow)

class ContactMessage(Base):
    __tablename__ = "contact_messages"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    message = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    is_read = Column(Boolean, default=False)

class Certificate(Base):
    __tablename__ = "certificates"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    organization = Column(String(200), nullable=False)
    year = Column(String(50), nullable=False)
    description = Column(Text)
    certificate_url = Column(String(300))
    created_at = Column(DateTime, default=datetime.utcnow)
