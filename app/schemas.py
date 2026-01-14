from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class EducationBase(BaseModel):
    school_name: str
    degree: str
    year: str
    achievements: Optional[str] = None

class EducationCreate(EducationBase):
    pass

class Education(EducationBase):
    id: int
    created_at: datetime
    
    class Config:
        from_attributes = True

class SkillBase(BaseModel):
    name: str
    category: str
    level: str
    description: Optional[str] = None

class SkillCreate(SkillBase):
    pass

class Skill(SkillBase):
    id: int
    created_at: datetime
    
    class Config:
        from_attributes = True

class ProjectBase(BaseModel):
    title: str
    description: str
    technologies: str
    github_link: Optional[str] = None
    demo_link: Optional[str] = None
    image_url: Optional[str] = None

class ProjectCreate(ProjectBase):
    pass

class Project(ProjectBase):
    id: int
    created_at: datetime
    
    class Config:
        from_attributes = True

class ExperienceBase(BaseModel):
    title: str
    company: Optional[str] = None
    location: Optional[str] = None
    start_date: Optional[str] = None
    end_date: Optional[str] = None
    description: Optional[str] = None
    type: Optional[str] = None

class ExperienceCreate(ExperienceBase):
    pass

class Experience(ExperienceBase):
    id: int
    created_at: datetime
    
    class Config:
        from_attributes = True

class ContactMessageBase(BaseModel):
    name: str
    email: EmailStr
    message: str

class ContactMessageCreate(ContactMessageBase):
    pass

class ContactMessage(ContactMessageBase):
    id: int
    created_at: datetime
    is_read: bool
    
    class Config:
        from_attributes = True


class CertificateBase(BaseModel):
    title: str
    organization: str
    year: str
    description: Optional[str] = None
    certificate_url: Optional[str] = None

class CertificateCreate(CertificateBase):
    pass

class Certificate(CertificateBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True