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

# Sample data endpoint
@router.get("/education/sample")
def get_sample_education():
    return [
        {
            "id": 1,
            "school_name": "សាកលវិទ្យាល័យភូមិន្ទភ្នំពេញ",
            "degree": "វិស្វករគំរូព័ត៌មាន",
            "year": "2022-2026",
            "achievements": "ជាប់ពិន្ទុ A ក្នុងវគ្គ Web Development\nសិស្សពូកែផ្នែក Programming",
            "created_at": "2025-01-01T00:00:00"
        },
        {
            "id": 2,
            "school_name": "វិទ្យាល័យព្រះស៊ីសុវត្ថិ",
            "degree": "វិទ្យាសាស្ត្រ-គណិតវិទ្យា",
            "year": "2016-2022",
            "achievements": "សិស្សពូកែថ្នាក់ជាតិ\nបានបញ្ចប់ជាប់ពិន្ទុ GPA 3.8",
            "created_at": "2025-01-01T00:00:00"
        }
    ]