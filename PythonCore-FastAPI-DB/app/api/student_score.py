from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.models.student_score import StudentScore
from app.schemas.student_score import (
    StudentScoreCreate,
    StudentScoreUpdate,
    StudentScoreResponse,
)

router = APIRouter(prefix="/student_scores", tags=["StudentScores"])


@router.get("/", response_model=List[StudentScoreResponse])
def get_scores(db: Session = Depends(get_db)):
    return db.query(StudentScore).all()


@router.get("/{score_id}", response_model=StudentScoreResponse)
def get_score(score_id: int, db: Session = Depends(get_db)):
    score = db.query(StudentScore).filter(StudentScore.score_id == score_id).first()
    if not score:
        raise HTTPException(status_code=404, detail="score not found")
    return score


@router.post("/", response_model=StudentScoreResponse)
def create_score(payload: StudentScoreCreate, db: Session = Depends(get_db)):
    score = StudentScore(
        student_id=payload.student_id,
        tamil=payload.tamil,
        english=payload.english,
        maths=payload.maths,
        science=payload.science,
        socail_science=payload.socail_science,
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
    score.student_id = payload.student_id
    score.tamil = payload.tamil
    score.english = payload.english
    score.maths = payload.maths
    score.science = payload.science
    score.socail_science = payload.socail_science
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
