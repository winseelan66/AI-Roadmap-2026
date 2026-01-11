from pydantic import BaseModel
from datetime import date, datetime
from typing import Optional

class StudentCreate(BaseModel):
    first_name: str
    last_name: Optional[str]
    dob: date
    sex_id: Optional[int]
    modified_date: datetime

class StudentUpdate(BaseModel):
    first_name: str
    last_name: Optional[str]
    dob: date
    sex_id: Optional[int]
    modified_date: datetime

class StudentResponse(BaseModel):
    student_id: int
    first_name: str
    last_name: Optional[str]
    dob: date
    sex_id: Optional[int]
    modified_date: datetime

    class Config:
        orm_mode = True
