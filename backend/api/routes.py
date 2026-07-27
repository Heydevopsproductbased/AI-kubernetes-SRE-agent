from fastapi import APIRouter
from backend.app.schemas import IncidentRequest
from backend.agents.incident_agent import analyze_incident

router = APIRouter()

@router.get("/")
def root():
    return {"message": "AI-kubernetes-SRE-agent is running"}

@router.get("/health")
def health_check():
    return {"status": "ok"}

@router.post("/analyze")
def analyze(payload: IncidentRequest):
    return analyze_incident(
        namespace=payload.namespace,
        pod_name=payload.pod_name,
        issue_type=payload.issue_type,
    )