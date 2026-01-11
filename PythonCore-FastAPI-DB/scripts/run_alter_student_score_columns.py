import sys
from pathlib import Path

project_root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(project_root))

from sqlalchemy import text
from app.database import engine

SQL = [
    "ALTER TABLE dbo.student_score ALTER COLUMN tamil decimal(5,2) NOT NULL;",
    "ALTER TABLE dbo.student_score ALTER COLUMN english decimal(5,2) NOT NULL;",
    "ALTER TABLE dbo.student_score ALTER COLUMN maths decimal(5,2) NOT NULL;",
    "ALTER TABLE dbo.student_score ALTER COLUMN science decimal(5,2) NOT NULL;",
    "ALTER TABLE dbo.student_score ALTER COLUMN socail_science decimal(5,2) NOT NULL;",
]


def main():
    print('Connecting to database via SQLAlchemy engine...')
    try:
        with engine.begin() as conn:
            for stmt in SQL:
                print('Executing:', stmt)
                conn.execute(text(stmt))
        print('ALTER TABLE statements executed successfully.')
    except Exception as e:
        print('Error executing ALTER statements:')
        raise


if __name__ == '__main__':
    main()
