from fastapi import FastAPI
from agent.agent_main import graph

app = FastAPI()

@app.get("/")
def root():
    return {"message": "DeliveryOps Agent is live."}

@app.post("/run-agent")
async def run_agent():
    state = {"project_status": {}, "risks": [], "alerts": []}
    results = []
    async for item in graph.astream(state):
        results.append(item)
    return results
