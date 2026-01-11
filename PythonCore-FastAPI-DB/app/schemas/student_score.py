from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class StudentScoreCreate(BaseModel):
    student_id: int
    tamil: float
    english: float
    maths: float
    science: float
    socail_science: float
    modified_date: Optional[datetime] = None


class StudentScoreUpdate(BaseModel):
    student_id: int
    tamil: float
    english: float
    maths: float
    science: float
    socail_science: float
    modified_date: Optional[datetime] = None


class StudentScoreResponse(BaseModel):
    score_id: int
    student_id: int
    tamil: float
    english: float
    maths: float
    science: float
    socail_science: float
    modified_date: datetime

    class Config:
        orm_mode = True

class StudentAggregateResponse(BaseModel):
    student_id: int
    total_score: float
    average_score: float

    class Config:
        orm_mode = True
