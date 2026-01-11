from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.core.database import get_db
from app.models.sex import Sex
from app.schemas.sex import SexResponse

router = APIRouter(prefix="/sex", tags=["Sex"])

@router.get("/", response_model=List[SexResponse])
def get_sex(db: Session = Depends(get_db)):
    return db.query(Sex).all()
