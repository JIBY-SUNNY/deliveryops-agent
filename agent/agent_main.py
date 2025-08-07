from langgraph.graph import StateGraph, END
from agent.agent_nodes import fetch_status, check_risks, emit_alerts, record_snapshot
from typing import TypedDict, List, Dict, Any

# Define state schema
class AgentState(TypedDict, total=False):
    project_status: Dict[str, Any]
    risks: List[str]
    alerts: List[str]

# Build the graph
builder = StateGraph(AgentState)

builder.add_node("fetch_status", fetch_status)
builder.add_node("check_risks", check_risks)
builder.add_node("emit_alerts", emit_alerts)
builder.add_node("record_snapshot", record_snapshot)

builder.set_entry_point("fetch_status")

builder.add_edge("fetch_status", "check_risks")
builder.add_edge("check_risks", "emit_alerts")
builder.add_edge("emit_alerts", "record_snapshot")
builder.add_edge("record_snapshot", END)

graph = builder.compile()
