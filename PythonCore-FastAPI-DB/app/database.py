from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = (
    "mssql+pyodbc://@DESKTOP-SPB2C2V/AI_Roadmap"
    "?driver=ODBC+Driver+17+for+SQL+Server"
    "&trusted_connection=yes"
)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
# Import all models here so they are registered with the shared `Base` metadata
# This ensures ForeignKey relationships resolve even if a model module hasn't
# been imported elsewhere before a DB operation.
import app.models.sex  # noqa: F401
import app.models.student  # noqa: F401
import app.models.student_score  # noqa: F401


def get_db():
    """Dependency that yields a SQLAlchemy Session and ensures it is closed."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
