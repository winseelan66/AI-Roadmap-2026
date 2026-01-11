from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models.student import Student
from app.schemas.student import StudentCreate, StudentUpdate, StudentResponse

router = APIRouter(prefix="/student", tags=["student"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[StudentResponse])
def get_all_student(db: Session = Depends(get_db)):
    return db.query(Student).all()

@router.get("/{student_id}", response_model=StudentResponse)
def get_student_by_id(student_id: int, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.student_id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="student not found")
    return student


@router.post("/", response_model=StudentResponse)
def create_student(payload: StudentCreate, db: Session = Depends(get_db)):
    student = Student(first_name=payload.first_name, last_name=payload.last_name, dob=payload.dob, sex_id=payload.sex_id, modified_date=payload.modified_date)
    db.add(student)
    db.commit()
    db.refresh(student)
    return student


@router.put("/{student_id}", response_model=StudentResponse)
def update_student(student_id: int, payload: StudentUpdate, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.student_id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="student not found")

    student.first_name = payload.first_name
    student.last_name = payload.last_name
    student.dob = payload.dob
    student.sex_id = payload.sex_id
    student.modified_date = payload.modified_date
    db.commit()
    db.refresh(student)
    return student


@router.delete("/{student_id}")
def delete_student(student_id: int, db: Session = Depends(get_db)):
    student = db.query(Student).filter(student.student_id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="student not found")
    try:
        db.delete(student)
        db.commit()
        return {"message": "student Deleted successfully"}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))
