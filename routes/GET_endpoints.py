from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List
import schemas
from database import get_db
from models import r0971085_match, r0971085_communityEvent
from typing import List, Optional

router = APIRouter()

@router.get("/matches/", response_model=List[schemas.Match])
def read_matches(skip: int = 0, limit: int = 10, database: Session = Depends(get_db)):
    try:
        matches = database.query(r0971085_match.Match).offset(skip).limit(limit).all()
        return matches
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred while reading matches: {str(e)}")


@router.get("/match/", response_model=Optional[schemas.Match])
def read_match_by_id(id: Optional[int] = Query(None), database: Session = Depends(get_db)):
    if id is None:
        raise HTTPException(status_code=400, detail="Query parameter 'id' is required.")
    
    try:
        match = database.query(r0971085_match.Match).filter(r0971085_match.Match.id == id).first()
        if match is None:
            raise HTTPException(status_code=404, detail="Match not found")
        return match
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred while reading the match: {str(e)}")

@router.get("/communityevents/", response_model=List[schemas.CommunityEvent])
def read_events(skip: int = 0, limit: int = 10, database: Session = Depends(get_db)):
    try:
        events = database.query(r0971085_communityEvent.CommunityEvent).offset(skip).limit(limit).all()
        return events
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred while reading events: {str(e)}")