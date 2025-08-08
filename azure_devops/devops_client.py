import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

load_dotenv()

AZURE_PAT = os.getenv("AZURE_PAT")
AZURE_ORG = os.getenv("AZURE_ORG")
AZURE_PROJECT = os.getenv("AZURE_PROJECT")

BASE_URL = f"https://dev.azure.com/{AZURE_ORG}"
auth = HTTPBasicAuth("", AZURE_PAT)
headers = {"Content-Type": "application/json"}

def get_project_status():
    url = f"{BASE_URL}/_apis/projects/{AZURE_PROJECT}?api-version=7.0"
    response = requests.get(url, auth=auth, headers=headers)
    response.raise_for_status()
    return response.json()
