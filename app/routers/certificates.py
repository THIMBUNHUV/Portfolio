from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app import crud, schemas
from app.database import get_db

router = APIRouter()

@router.get("/certificates", response_model=List[schemas.Certificate])
def read_certificates(db: Session = Depends(get_db)):
    return crud.get_certificates(db)

@router.post("/certificates", response_model=schemas.Certificate)
def create_certificate(
    certificate: schemas.CertificateCreate,
    db: Session = Depends(get_db)
):
    return crud.create_certificate(db, certificate)
