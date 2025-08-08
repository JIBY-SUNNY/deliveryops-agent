from fastapi import FastAPI
from agent.agent_main import graph  # import your LangGraph
from typing import Dict, Any
import uuid
import json
import os

app = FastAPI()

SNAPSHOT_DIR = "snapshots"
os.makedirs(SNAPSHOT_DIR, exist_ok=True)

@app.get("/")
def root():
    return {"message": "DeliveryOps Agent API running"}

@app.post("/status")
async def get_status():
    # 1. Run the agent
    result = graph.invoke({})  # empty initial state

    # 2. Create snapshot ID
    snapshot_id = str(uuid.uuid4())

    # 3. Save result to file
    with open(f"{SNAPSHOT_DIR}/{snapshot_id}.json", "w") as f:
        json.dump(result, f, indent=2)

    return {
        "status": "completed",
        "snapshot_id": snapshot_id,
        "result": result
    }
