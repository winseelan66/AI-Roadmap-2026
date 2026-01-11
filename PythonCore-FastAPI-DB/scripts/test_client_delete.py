import sys, traceback
sys.path.insert(0, r'C:\Users\Admin\Documents\AI-Roadmap-2026\PythonCore-FastAPI-DB')
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)
try:
    r = client.delete('/student/1')
    print('status', r.status_code)
    print('headers', r.headers)
    print('body', r.text)
except Exception as e:
    print('EXCEPTION', type(e).__name__, str(e))
    traceback.print_exc()
