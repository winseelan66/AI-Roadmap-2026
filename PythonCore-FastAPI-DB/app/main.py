import sys
from pathlib import Path

# Ensure project root is on sys.path so subprocesses (uvicorn reload) can import `app`
project_root = str(Path(__file__).resolve().parents[1])
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from fastapi import FastAPI
from app.routers import sex
from app.routers import student

app = FastAPI(title="PythonCore FastAPI DB")

app.include_router(sex.router)
app.include_router(student.router)

@app.get("/")
def root():
    return {"status": "API is running"}
