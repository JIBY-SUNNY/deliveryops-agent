import os
from dotenv import load_dotenv
import requests
from requests.auth import HTTPBasicAuth

# Load env vars from .env
load_dotenv()

AZURE_PAT = os.getenv("AZURE_PAT")
AZURE_ORG = os.getenv("AZURE_ORG")
AZURE_PROJECT = os.getenv("AZURE_PROJECT")

BASE_URL = f"https://dev.azure.com/{AZURE_ORG}"
auth = HTTPBasicAuth("", AZURE_PAT)
headers = {
    "Content-Type": "application/json"
}

def get_work_items():
    url = f"{BASE_URL}/{AZURE_PROJECT}/_apis/wit/workitems?ids=1,2,3&api-version=7.1-preview.3"
    response = requests.get(url, auth=auth, headers=headers)

    if response.status_code != 200:
        return {"error": "Failed to fetch work items", "details": response.text}

    data = response.json()
    return {
        "work_items": [
            {
                "id": item["id"],
                "title": item["fields"].get("System.Title", "N/A"),
                "state": item["fields"].get("System.State", "Unknown")
            }
            for item in data.get("value", [])
        ]
    }


def get_iterations():
    url = f"{BASE_URL}/{AZURE_PROJECT}/_apis/work/teamsettings/iterations?$timeframe=current&api-version=7.1-preview.1"
    response = requests.get(url, auth=auth, headers=headers)

    if response.status_code != 200:
        return {"error": "Failed to fetch iterations", "details": response.text}

    data = response.json()
    current = data.get("value", [{}])[0]

    return {
        "name": current.get("name"),
        "startDate": current.get("attributes", {}).get("startDate"),
        "endDate": current.get("attributes", {}).get("finishDate")
    }

def get_pipeline_status(pipeline_id=1):
    url = f"{BASE_URL}/{AZURE_PROJECT}/_apis/pipelines/{pipeline_id}/runs?api-version=7.1-preview.1"
    response = requests.get(url, auth=auth, headers=headers)

    if response.status_code != 200:
        return {"error": "Failed to fetch pipeline status", "details": response.text}

    data = response.json()
    latest_run = data.get("value", [])[0]

    return {
        "pipeline_id": pipeline_id,
        "status": latest_run.get("state"),
        "result": latest_run.get("result"),
        "created": latest_run.get("createdDate")
    }

