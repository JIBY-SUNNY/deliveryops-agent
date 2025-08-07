from azure_devops.devops_client import get_project_status

def fetch_status(state):
    status = get_project_status()
    return {"project_status": status}

def check_risks(state):
    status = state.get("project_status", {})
    risks = []

    if status.get("milestone_due") and not status.get("progress"):
        risks.append("Milestone is overdue but no progress recorded.")
    if status.get("blocked_items", 0) > 3:
        risks.append("Multiple items are marked as blocked.")

    return {"risks": risks}

def emit_alerts(state):
    alerts = []
    for risk in state.get("risks", []):
        alerts.append(f"ALERT: {risk}")
    return {"alerts": alerts}

def record_snapshot(state):
    print("Snapshot:", state)
    return {}

from utils.azure_devops import get_work_items, get_iterations, get_pipeline_status

def extract_project_status(state):
    work_items = get_work_items()
    sprint = get_iterations()
    pipeline = get_pipeline_status()

    return {
        "project_status": {
            "work_items": work_items,
            "current_sprint": sprint,
            "pipeline_status": pipeline
        },
        "risks": [],
        "alerts": []
    }
