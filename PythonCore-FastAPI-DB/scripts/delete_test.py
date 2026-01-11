import sys, traceback
sys.path.insert(0, r'C:\Users\Admin\Documents\AI-Roadmap-2026\PythonCore-FastAPI-DB')
from app.database import SessionLocal
from app.models.student import Student

if __name__ == '__main__':
    db = SessionLocal()
    try:
        s = db.query(Student).filter(Student.student_id == 1).first()
        print('found:', bool(s))
        if s:
            db.delete(s)
            db.commit()
            print('deleted')
        else:
            print('no student to delete')
    except Exception as e:
        db.rollback()
        print('EXCEPTION:', type(e).__name__, str(e))
        traceback.print_exc()
    finally:
        db.close()
