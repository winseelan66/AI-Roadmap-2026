import sys, traceback
from decimal import Decimal
sys.path.insert(0, r'C:\Users\Admin\Documents\AI-Roadmap-2026\PythonCore-FastAPI-DB')
from app.database import SessionLocal
from app.models.student_score import StudentScore

if __name__ == '__main__':
    db = SessionLocal()
    try:
        score = StudentScore(
            student_id=2,
            tamil=Decimal('100'),
            english=Decimal('52.36'),
            maths=Decimal('25'),
            science=Decimal('78'),
            socail_science=Decimal('95'),
        )
        db.add(score)
        db.commit()
        db.refresh(score)
        print('Inserted score id:', score.score_id)
    except Exception as e:
        db.rollback()
        print('EXCEPTION:', type(e).__name__, str(e))
        traceback.print_exc()
    finally:
        db.close()
