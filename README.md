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
