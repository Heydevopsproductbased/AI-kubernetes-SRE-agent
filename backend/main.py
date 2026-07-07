from fastapi import FastAPI
from backend.api.routes import router

app = FastAPI(
    title="AI-kubernetes-SRE-agent",
    description="AI-powered Kubernetes troubleshooting agent for incident diagnosis and remediation suggestions.",
    version="0.1.0",
)

app.include_router(router)
