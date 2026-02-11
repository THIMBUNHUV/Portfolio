from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app import crud, schemas
from app.database import get_db

router = APIRouter()

@router.get("/education", response_model=List[schemas.Education])
def read_educations(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    educations = crud.get_educations(db, skip=skip, limit=limit)
    return educations

@router.post("/education", response_model=schemas.Education)
def create_education(education: schemas.EducationCreate, db: Session = Depends(get_db)):
    return crud.create_education(db=db, education=education)