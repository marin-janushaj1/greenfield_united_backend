from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import date, time

class MatchBase(BaseModel):
    home_team: str
    away_team: str
    match_date: date
    match_time: time
    home_team_score: int = 0
    away_team_score: int = 0

class MatchCreate(MatchBase):
    pass

class Match(MatchBase):
    id: int

    class Config:
        orm_mode = True

class CommunityEventBase(BaseModel):
    event_name: str
    event_date: date
    event_time: time
    location: str
    description: Optional[str] = None
    organizer: Optional[str] = None
    contact_info: Optional[str] = None

class CommunityEventCreate(CommunityEventBase):
    pass

class CommunityEvent(CommunityEventBase):
    id: int

    class Config:
        orm_mode = True

class ContactForm(BaseModel):
    fullname: str
    subject: str
    phone: str
    email: EmailStr
    message: str

