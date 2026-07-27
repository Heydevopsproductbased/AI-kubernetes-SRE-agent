from pydantic import BaseModel

class IncidentRequest(BaseModel):
    namespace: str
    pod_name: str
    issue_type: str