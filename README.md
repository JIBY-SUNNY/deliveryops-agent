# DeliveryOps Agent

LangGraph-based agent to automate project status reporting, milestone tracking, and risk alerting. Integrates with Azure DevOps MCP.

## 🧠 Core Features
- Extracts project status and milestones from Azure DevOps
- Flags risks based on configurable logic
- Sends alerts (email, Slack, Teams)
- React dashboard shows real-time status and milestones

## 🧱 Architecture
- LangGraph handles reactive state flow
- FastAPI backend
- React frontend
- Azure DevOps MCP integration

## 🚀 Quickstart

### Backend (Python)
```bash
pip install -r requirements.txt
cp .env.example .env  # Add your credentials
uvicorn api.main:app --reload
