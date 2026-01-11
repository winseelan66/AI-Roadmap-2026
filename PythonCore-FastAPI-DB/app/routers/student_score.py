from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import SessionLocal
from app.models.student_score import StudentScore
from decimal import Decimal, InvalidOperation
from app.schemas.student_score import (
    StudentScoreCreate,
    StudentScoreUpdate,
    StudentScoreResponse,
)

router = APIRouter(prefix="/student_score", tags=["StudentScore"]) 


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=List[StudentScoreResponse])
def get_all_scores(db: Session = Depends(get_db)):
    return db.query(StudentScore).all()


@router.get("/{score_id}", response_model=StudentScoreResponse)
def get_score_by_id(score_id: int, db: Session = Depends(get_db)):
    score = db.query(StudentScore).filter(StudentScore.score_id == score_id).first()
    if not score:
        raise HTTPException(status_code=404, detail="score not found")
    return score


@router.post("/", response_model=StudentScoreResponse)
def create_score(payload: StudentScoreCreate, db: Session = Depends(get_db)):
    # convert and validate numeric fields
    try:
        tamil = Decimal(str(payload.tamil))
        english = Decimal(str(payload.english))
        maths = Decimal(str(payload.maths))
        science = Decimal(str(payload.science))
        socail_science = Decimal(str(payload.socail_science))
    except (InvalidOperation, TypeError):
        raise HTTPException(status_code=400, detail="Invalid numeric value")

    MAX = Decimal("999.99")
    for v in (tamil, english, maths, science, socail_science):
        if v.copy_abs() > MAX:
            raise HTTPException(status_code=400, detail=f"Score value {v} out of allowed range <= {MAX}")

    score = StudentScore(
        student_id=payload.student_id,
        tamil=tamil,
        english=english,
        maths=maths,
        science=science,
        socail_science=socail_science,
        modified_date=payload.modified_date,
    )
    db.add(score)
    db.commit()
    db.refresh(score)
    return score


@router.put("/{score_id}", response_model=StudentScoreResponse)
def update_score(score_id: int, payload: StudentScoreUpdate, db: Session = Depends(get_db)):
    score = db.query(StudentScore).filter(StudentScore.score_id == score_id).first()
    if not score:
        raise HTTPException(status_code=404, detail="score not found")
    try:
        tamil = Decimal(str(payload.tamil))
        english = Decimal(str(payload.english))
        maths = Decimal(str(payload.maths))
        science = Decimal(str(payload.science))
        socail_science = Decimal(str(payload.socail_science))
    except (InvalidOperation, TypeError):
        raise HTTPException(status_code=400, detail="Invalid numeric value")

    MAX = Decimal("999.99")
    for v in (tamil, english, maths, science, socail_science):
        if v.copy_abs() > MAX:
            raise HTTPException(status_code=400, detail=f"Score value {v} out of allowed range <= {MAX}")

    score.student_id = payload.student_id
    score.tamil = tamil
    score.english = english
    score.maths = maths
    score.science = science
    score.socail_science = socail_science
    score.modified_date = payload.modified_date
    db.commit()
    db.refresh(score)
    return score


@router.delete("/{score_id}")
def delete_score(score_id: int, db: Session = Depends(get_db)):
    score = db.query(StudentScore).filter(StudentScore.score_id == score_id).first()
    if not score:
        raise HTTPException(status_code=404, detail="score not found")
    try:
        db.delete(score)
        db.commit()
        return {"message": "score Deleted successfully"}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))
