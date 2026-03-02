from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from core.orchestrator import Orchestrator
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
app = FastAPI(
    title="Overlord API",
    description="AI Agent Platform for Dev Teams",
    version="1.0.0"
    
)
app.mount("/static", StaticFiles(directory="dashboard"), name="static")

@app.get("/dashboard")
def serve_dashboard():
    return FileResponse("dashboard/index.html")

orchestrator = Orchestrator()

class DevRequest(BaseModel):
    request: str

@app.get("/")
def root():
    return {
        "status": "Overlord is running",
        "version": "1.0.0"
    }

@app.post("/generate")
def generate(dev_request: DevRequest):
    try:
        result = orchestrator.process(dev_request.request)
        return {
            "success": True,
            "data": result
        }
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail={
                "error": str(e),
                "type": type(e).__name__,
                "suggestion": "Check Gemini API key and model availability."
            }
        )