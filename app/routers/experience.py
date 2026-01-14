from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models import Experience
from app import schemas
from app.database import get_db

router = APIRouter()


@router.get("/experience", response_model=list[schemas.Experience])
def get_experience(db: Session = Depends(get_db)):
    return db.query(Experience).all()

@router.post("/experience", response_model=schemas.Experience)
def create_experience(
    exp: schemas.ExperienceCreate,
    db: Session = Depends(get_db)
):
    new_exp = Experience(**exp.dict())
    db.add(new_exp)
    db.commit()
    db.refresh(new_exp)
    return new_exp
