import sys, traceback
sys.path.insert(0, r'C:\Users\Admin\Documents\AI-Roadmap-2026\PythonCore-FastAPI-DB')
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)
payload = {
    "student_id": 2,
    "tamil": 58,
    "english": 65,
    "maths": 47,
    "science": 89,
    "socail_science": 89,
    "modified_date": "2026-01-11T07:31:49.593Z"
}
try:
    r = client.post('/student_score/', json=payload)
    print('status', r.status_code)
    print('headers', dict(r.headers))
    print('body', r.text)
    if r.status_code >= 500:
        print('DETAILS:', r.json() if r.headers.get('content-type','').startswith('application/json') else r.text)
except Exception as e:
    print('EXCEPTION', type(e).__name__, str(e))
    traceback.print_exc()
