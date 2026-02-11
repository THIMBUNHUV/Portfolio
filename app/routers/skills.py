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
