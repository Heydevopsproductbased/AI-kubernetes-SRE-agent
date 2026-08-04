from typing import Dict


def analyze_incident(namespace: str, pod_name: str, issue_type: str) -> Dict:
    """
    Simple rule-based incident analysis.

    This version does NOT talk to Kubernetes directly.
    It just uses the namespace, pod_name, and issue_type to
    generate a probable cause and recommended action.
    """

    issue = (issue_type or "").lower()

    if issue == "crashloopbackoff":
        probable_cause = (
            f"Possible CrashLoopBackOff issue detected in pod {pod_name}."
        )
        recommended_action = (
            "Check container logs, recent config/image changes, probes, and resource limits."
        )

    elif issue == "imagepullbackoff":
        probable_cause = (
            f"Possible ImagePullBackOff issue detected in pod {pod_name}."
        )
        recommended_action = (
            "Verify image name and tag, registry URL, network access to the registry, "
            "and imagePullSecrets for private registries."
        )

    elif issue == "oomkilled":
        probable_cause = (
            f"Possible OOMKilled issue detected in pod {pod_name}."
        )
        recommended_action = (
            "Inspect memory usage, increase Pod memory limits if needed, "
            "and check for memory leaks or large in-memory caches."
        )

    else:
        probable_cause = (
            f"Unknown issue type '{issue_type}' for pod {pod_name}."
        )
        recommended_action = (
            "Check pod status, events (`kubectl describe pod`) and container logs "
            "to get more detailed error information."
        )

    return {
        "namespace": namespace,
        "pod_name": pod_name,
        "issue_type": issue_type,
        "probable_cause": probable_cause,
        "recommended_action": recommended_action,
    }