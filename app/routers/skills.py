from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app import crud, schemas
from app.database import get_db

router = APIRouter()

@router.get("/skills", response_model=List[schemas.Skill])
def read_skills(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    skills = crud.get_skills(db, skip=skip, limit=limit)
    return skills

@router.get("/skills/{category}")
def read_skills_by_category(category: str, db: Session = Depends(get_db)):
    skills = crud.get_skills_by_category(db, category=category)
    return skills

@router.post("/skills", response_model=schemas.Skill)
def create_skill(skill: schemas.SkillCreate, db: Session = Depends(get_db)):
    return crud.create_skill(db=db, skill=skill)

@router.get("/skills/sample")
def get_sample_skills():
    return {
        "technical": [
            {
                "name": "HTML/CSS",
                "level": "advanced",
                "description": "អាចបង្កើតគេហទំព័រស្តាទិកនិងឌីណាមិក"
            },
            {
                "name": "JavaScript",
                "level": "intermediate",
                "description": "អាចសរសេរកូដសម្រាប់ដំណើរការនៅលើ client-side"
            },
            {
                "name": "Python",
                "level": "intermediate",
                "description": "អាចបង្កើត API និង scripts"
            },
            {
                "name": "FastAPI",
                "level": "basic",
                "description": "អាចបង្កើត RESTful API"
            },
            {
                "name": "PostgreSQL",
                "level": "basic",
                "description": "អាចរចនា database និងសរសេរ SQL queries"
            },
            {
                "name": "Git",
                "level": "intermediate",
                "description": "អាចប្រើប្រាស់ Git សម្រាប់ version control"
            }
        ],
        "soft": [
            {
                "name": "ការសម្របសម្រួលការងារក្រុម",
                "level": "advanced",
                "description": "អាចធ្វើការជាមួយក្រុមបានល្អ"
            },
            {
                "name": "ការទំនាក់ទំនង",
                "level": "advanced",
                "description": "អាចបញ្ជាក់គំនិតដោយច្បាស់លាស់"
            },
            {
                "name": "ការដោះស្រាយបញ្ហា",
                "level": "intermediate",
                "description": "អាចរកដំណោះស្រាយចំពោះបញ្ហាបច្ចេកទេស"
            },
            {
                "name": "ការគ្រប់គ្រងពេលវេលា",
                "level": "intermediate",
                "description": "អាចរៀបចំការងារឱ្យបានល្អ"
            }
        ]
    }