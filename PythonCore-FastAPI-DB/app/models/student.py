from sqlalchemy import Column, Integer, String, Date, DateTime, ForeignKey
from datetime import datetime
from app.database import Base

class Student(Base):
    __tablename__ = "Student"

    student_id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50))
    dob = Column(Date, nullable=False)
    sex_id = Column(Integer, ForeignKey("Sex.sex_id"))
    modified_date = Column(DateTime, default=datetime.utcnow)
