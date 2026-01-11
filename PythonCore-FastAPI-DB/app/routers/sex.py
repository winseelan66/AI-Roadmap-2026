from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models.sex import Sex
from app.schemas.sex import SexCreate, SexUpdate, SexResponse

router = APIRouter(prefix="/sex", tags=["Sex"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[SexResponse])
def get_all_sex(db: Session = Depends(get_db)):
    return db.query(Sex).all()

@router.get("/{sex_id}", response_model=SexResponse)
def get_sex_by_id(sex_id: int, db: Session = Depends(get_db)):
    sex = db.query(Sex).filter(Sex.sex_id == sex_id).first()
    if not sex:
        raise HTTPException(status_code=404, detail="Sex not found")
    return sex


@router.post("/", response_model=SexResponse)
def create_sex(payload: SexCreate, db: Session = Depends(get_db)):
    sex = Sex(name=payload.name)
    db.add(sex)
    db.commit()
    db.refresh(sex)
    return sex


@router.put("/{sex_id}", response_model=SexResponse)
def update_sex(sex_id: int, payload: SexUpdate, db: Session = Depends(get_db)):
    sex = db.query(Sex).filter(Sex.sex_id == sex_id).first()
    if not sex:
        raise HTTPException(status_code=404, detail="Sex not found")

    sex.name = payload.name
    db.commit()
    db.refresh(sex)
    return sex


@router.delete("/{sex_id}")
def delete_sex(sex_id: int, db: Session = Depends(get_db)):
    sex = db.query(Sex).filter(Sex.sex_id == sex_id).first()
    if not sex:
        raise HTTPException(status_code=404, detail="Sex not found")

    db.delete(sex)
    db.commit()
    return {"message": "Deleted successfully"}
