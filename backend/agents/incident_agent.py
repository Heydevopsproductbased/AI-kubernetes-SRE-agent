def analyze_incident(namespace: str, pod_name: str, issue_type: str) -> dict:
    return {
        "namespace": namespace,
        "pod_name": pod_name,
        "issue_type": issue_type,
        "probable_cause": f"Possible {issue_type} issue detected in pod {pod_name}.",
        "recommended_action": "Check logs, events, probes, and resource limits.",
    }