from sqlalchemy import Column, Integer, DateTime, ForeignKey, Numeric
from datetime import datetime
from app.database import Base


class StudentScore(Base):
    __tablename__ = "student_score"

    score_id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("Student.student_id"), nullable=False)
    tamil = Column(Numeric(3, 2), nullable=False)
    english = Column(Numeric(3, 2), nullable=False)
    maths = Column(Numeric(3, 2), nullable=False)
    science = Column(Numeric(3, 2), nullable=False)
    socail_science = Column(Numeric(3, 2), nullable=False)
    modified_date = Column(DateTime, default=datetime.utcnow)
