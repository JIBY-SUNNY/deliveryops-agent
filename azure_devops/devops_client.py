import requests
import os
from dotenv import load_dotenv
load_dotenv()

ADO_ORG = os.getenv("ADO_ORG")
ADO_PROJECT = os.getenv("ADO_PROJECT")
ADO_PAT = os.getenv("ADO_PAT")
ADO_API = f"https://dev.azure.com/{ADO_ORG}/{ADO_PROJECT}/_apis"

headers = {
    "Authorization": f"Basic {os.getenv('ADO_BASIC_AUTH')}",
    "Content-Type": "application/json"
}

def get_project_status():
    # Placeholder for now
    return {
        "milestone_due": True,
        "progress": False,
        "blocked_items": 4
    }
