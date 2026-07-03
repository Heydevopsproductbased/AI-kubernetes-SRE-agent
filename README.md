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
├── README.md
├── LICENSE
├── .gitignore
├── .env.example
├── requirements.txt
├── pyproject.toml
├── Dockerfile
├── docker-compose.yml
├── Makefile
├── backend/
│   ├── main.py
│   ├── app/
│   │   ├── __init__.py
│   │   ├── config.py
│   │   ├── schemas.py
│   │   ├── dependencies.py
│   │   └── logging.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   └── health.py
│   ├── agents/
│   │   ├── __init__.py
│   │   ├── incident_agent.py
│   │   ├── diagnosis_agent.py
│   │   ├── remediation_agent.py
│   │   └── report_agent.py
│   ├── tools/
│   │   ├── __init__.py
│   │   ├── k8s_tools.py
│   │   ├── logs_tools.py
│   │   ├── metrics_tools.py
│   │   └── git_tools.py
│   ├── prompts/
│   │   ├── system_prompt.txt
│   │   ├── diagnosis_prompt.txt
│   │   └── remediation_prompt.txt
│   └── services/
│       ├── __init__.py
│       ├── incident_service.py
│       └── context_service.py
├── integrations/
│   ├── slack/
│   │   └── notifier.py
│   └── email/
│       └── notifier.py
├── k8s/
│   ├── namespaces/
│   │   └── namespace.yaml
│   ├── manifests/
│   │   ├── deployment.yaml
│   │   ├── service.yaml
│   │   └── configmap.yaml
│   ├── rbac/
│   │   ├── role.yaml
│   │   ├── rolebinding.yaml
│   │   └── serviceaccount.yaml
│   └── helm/
│       └── values.yaml
├── observability/
│   ├── prometheus/
│   │   └── prometheus-values.yaml
│   ├── grafana/
│   │   ├── dashboards/
│   │   └── datasources/
│   └── loki/
│       └── loki-values.yaml
├── tests/
│   ├── test_api.py
│   ├── test_agents.py
│   ├── test_tools.py
│   └── fixtures/
│       ├── pod_events.json
│       ├── pod_logs.txt
│       └── metrics.json
├── scripts/
│   ├── simulate_crashloop.sh
│   ├── simulate_oom.sh
│   └── demo_run.sh
├── docs/
│   ├── architecture.md
│   ├── use_cases.md
│   ├── incident_flow.md
│   ├── safety.md
│   └── screenshots/
└── examples/
├── sample_incident_input.json
└── sample_response.json

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
