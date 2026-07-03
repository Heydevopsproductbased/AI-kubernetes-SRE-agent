AI-kubernetes-SRE-agent
AI-powered Kubernetes troubleshooting agent for incident diagnosis, root-cause analysis, and fix recommendations.
Overview
AI-kubernetes-SRE-agent is a Kubernetes troubleshooting assistant that inspects pod status, events, logs, and metrics to help diagnose incidents faster. It is designed for DevOps, Platform Engineering, and SRE workflows, with a focus on observability-driven troubleshooting and clear remediation suggestions.
Why this project exists
Kubernetes incidents are hard to debug when you have to jump between events, logs, metrics, and deployment history. This project brings those signals together and helps explain what happened, why it happened, and what to do next.
Features
Reads Kubernetes pod events, logs, and status.
Detects common issues such as CrashLoopBackOff, OOMKilled, ImagePullBackOff, and failing probes.
Explains the likely root cause in simple language.
Suggests next-step fixes and safe remediation ideas.
Can generate a short incident summary report.
Built for observability-first troubleshooting.
Tech Stack
Python
FastAPI
Kubernetes Python client
Prometheus
Grafana
Loki
Docker
Optional LLM integration for reasoning and explanation
Folder Structure
kube-troubleshooting-agent/
├── backend/
├── integrations/
├── k8s/
├── observability/
├── tests/
├── scripts/
├── docs/
├── examples/
└── README.md
Getting Started
Prerequisites
Python 3.11+
Docker
kubectl
Access to a Kubernetes cluster for live troubleshooting
Git
Installation
```bash
git clone https://github.com/Heydevopsproductbased/AI-kubernetes-SRE-agent.git
cd AI-kubernetes-SRE-agent
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
Run locally
```bash
uvicorn backend.main:app --reload
```
Usage
Send an incident payload to the API and the agent will analyze it and return a diagnosis.
Example:
```json
{
  "namespace": "default",
  "pod_name": "demo-app-7d8f9f",
  "issue_type": "CrashLoopBackOff"
}
```
Example Output
The agent may respond with:
probable cause,
supporting evidence,
recommended fix,
follow-up checks.
Project Roadmap
[ ] Build the FastAPI API layer.
[ ] Add Kubernetes event and log readers.
[ ] Add metrics-based diagnosis.
[ ] Add incident report generation.
[ ] Add Grafana and Loki integrations.
[ ] Add Slack/email notifications.
[ ] Add optional safe auto-remediation.
Safety
The first version of this project should be read-only. It should diagnose and recommend, not change production systems automatically.
Contributing
Pull requests and issues are welcome. If you want to improve the agent, fork the repository and submit a PR.
License
MIT.
Contact
Project repository: AI-kubernetes-SRE-agent
