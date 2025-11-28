from src.agents.insight_agent import InsightAgent
import math

def test_insight_agent_handles_missing_key():
    agent = InsightAgent()
    summary = {}
    result = agent.generate_hypotheses(summary, retries=2)
    assert result[0]["issue"] == "Unknown"

def test_insight_agent_handles_none_ctr():
    agent = InsightAgent()
    summary = {"avg_ctr": None}
    result = agent.generate_hypotheses(summary, retries=2)
    assert result[0]["issue"] == "Unknown"

def test_insight_agent_handles_nan_ctr():
    agent = InsightAgent()
    summary = {"avg_ctr": float('nan')}
    result = agent.generate_hypotheses(summary, retries=2)
    assert result[0]["issue"] == "Unknown"

def test_insight_agent_handles_string_ctr():
    agent = InsightAgent()
    summary = {"avg_ctr": "invalid"}
    result = agent.generate_hypotheses(summary, retries=2)
    assert result[0]["issue"] == "Unknown"
