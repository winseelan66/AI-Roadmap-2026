import sys
from pathlib import Path

# Ensure project root is on sys.path so subprocesses (uvicorn reload) can import `app`
project_root = str(Path(__file__).resolve().parents[1])
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# Optional debugpy attachment: set environment variable DEBUGPY=1 to enable.
# Configure host/port with DEBUGPY_HOST and DEBUGPY_PORT. Set DEBUGPY_WAIT=1 to block until
# a debugger attaches.
import os
if os.getenv("DEBUGPY") == "1":
    try:
        import debugpy
        host = os.getenv("DEBUGPY_HOST", "0.0.0.0")
        port = int(os.getenv("DEBUGPY_PORT", "5678"))
        debugpy.listen((host, port))
        print(f"debugpy listening on {host}:{port}")
        if os.getenv("DEBUGPY_WAIT") == "1":
            print("Waiting for debugger to attach...")
            debugpy.wait_for_client()
    except Exception as e:
        print("debugpy not available:", e)

from fastapi import FastAPI
from app.routers import sex
from app.routers import student
from app.routers import student_score

app = FastAPI(title="PythonCore FastAPI DB")

app.include_router(sex.router)
app.include_router(student.router)
app.include_router(student_score.router)

@app.get("/")
def root():
    return {"status": "API is running"}
