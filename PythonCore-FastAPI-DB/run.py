"""Runner for debugging in VS Code.

Run with your venv Python (or use the VS Code debugger launch config) — reload is disabled
so the debugger doesn't lose the process.
"""
import uvicorn


if __name__ == "__main__":
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=False, log_level="debug")
