from sqlalchemy import Column, Integer, DateTime, CHAR
from datetime import datetime
from app.database import Base

class Sex(Base):
    __tablename__ = "Sex"

    sex_id = Column(Integer, primary_key=True, index=True)
    name = Column(CHAR(50), nullable=False)
    modified_date = Column(DateTime, default=datetime.utcnow)
