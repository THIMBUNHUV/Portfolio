from sqlalchemy.orm import Session
from app import models, schemas

# Education CRUD
def get_educations(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Education).offset(skip).limit(limit).all()

def create_education(db: Session, education: schemas.EducationCreate):
    db_education = models.Education(**education.dict())
    db.add(db_education)
    db.commit()
    db.refresh(db_education)
    return db_education

# Skills CRUD
def get_skills(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Skill).offset(skip).limit(limit).all()

def get_skills_by_category(db: Session, category: str):
    return db.query(models.Skill).filter(models.Skill.category == category).all()

def create_skill(db: Session, skill: schemas.SkillCreate):
    db_skill = models.Skill(**skill.dict())
    db.add(db_skill)
    db.commit()
    db.refresh(db_skill)
    return db_skill

# Projects CRUD
def get_projects(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Project).offset(skip).limit(limit).all()

def create_project(db: Session, project: schemas.ProjectCreate):
    db_project = models.Project(**project.dict())
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project

# Experience CRUD
def get_experiences(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Experience).offset(skip).limit(limit).all()

def create_experience(db: Session, experience: schemas.ExperienceCreate):
    db_experience = models.Experience(**experience.dict())
    db.add(db_experience)
    db.commit()
    db.refresh(db_experience)
    return db_experience

# Contact Messages CRUD
def get_contact_messages(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.ContactMessage).offset(skip).limit(limit).all()

def create_contact_message(db: Session, message: schemas.ContactMessageCreate):
    db_message = models.ContactMessage(**message.dict())
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    return db_message

def mark_message_as_read(db: Session, message_id: int):
    db_message = db.query(models.ContactMessage).filter(models.ContactMessage.id == message_id).first()
    if db_message:
        db_message.is_read = True
        db.commit()
        db.refresh(db_message)
    return db_message


def get_certificates(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Certificate).offset(skip).limit(limit).all()

def create_certificate(db: Session, certificate: schemas.CertificateCreate):
    db_cert = models.Certificate(**certificate.dict())
    db.add(db_cert)
    db.commit()
    db.refresh(db_cert)
    return db_cert

