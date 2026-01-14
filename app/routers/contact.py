from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app import crud, schemas
from app.database import get_db

router = APIRouter()

@router.get("/contact/messages", response_model=List[schemas.ContactMessage])
def read_contact_messages(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    messages = crud.get_contact_messages(db, skip=skip, limit=limit)
    return messages

@router.post("/contact", response_model=schemas.ContactMessage)
def create_contact_message(message: schemas.ContactMessageCreate, db: Session = Depends(get_db)):
    return crud.create_contact_message(db=db, message=message)

@router.put("/contact/messages/{message_id}/read")
def mark_as_read(message_id: int, db: Session = Depends(get_db)):
    message = crud.mark_message_as_read(db, message_id=message_id)
    if message is None:
        raise HTTPException(status_code=404, detail="Message not found")
    return {"message": "Message marked as read", "id": message_id}