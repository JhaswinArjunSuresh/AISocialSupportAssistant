from fastapi import FastAPI, UploadFile, File, Form
from pydantic import BaseModel
import joblib
import io
import json
from app.agents.orchestrator import Orchestrator
from app.agents.data_extraction import DataExtractor

app = FastAPI(title="Social Support AI Prototype")

# Load model artifact
MODEL_PATH = "app/models/eligibility_model.pkl"
try:
    model = joblib.load(MODEL_PATH)
except Exception as e:
    model = None
    print("Model not loaded:", e)

orchestrator = Orchestrator(model=model)

class Application(BaseModel):
    applicant_json: dict

@app.post("/api/assess")
async def assess_application(applicant_json: dict = Form(...), attachments: list[UploadFile] = File(None)):
    # attachments: bank statements, id scans, etc. Here we pass to extractor (mock)
    extractor = DataExtractor()
    extracted = {"form": applicant_json}
    # In real system, we would pass files to OCR and structured parsers.
    # Here we simulate by merging
    result = orchestrator.run(extracted)
    return result

@app.get("/api/health")
def health():
    return {"status": "ok"}

