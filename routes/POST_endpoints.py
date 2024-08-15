from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import schemas
from database import get_db
from models import r0971085_match, r0971085_communityEvent

router = APIRouter()

@router.post("/matches/", response_model=schemas.Match)
def create_match(matchCreate: schemas.MatchCreate, db: Session = Depends(get_db)):
    try:
        db_match = r0971085_match.Match(**matchCreate.dict())
        db.add(db_match)
        db.commit()
        db.refresh(db_match)
        return db_match
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"An error occurred while creating the match: {str(e)}")

@router.post("/communityevents/", response_model=schemas.CommunityEvent)
def create_event(event: schemas.CommunityEventCreate, database: Session = Depends(get_db)):
    try:
        db_event = r0971085_communityEvent.CommunityEvent(**event.dict())
        database.add(db_event)
        database.commit()
        database.refresh(db_event)
        return db_event
    except Exception as e:
        database.rollback()
        raise HTTPException(status_code=500, detail=f"An error occurred while creating the event: {str(e)}")

@router.post("/submit-form/")
async def submit_form(form_data: schemas.ContactForm):
    try:
        return {"status": "success", "data": form_data}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
