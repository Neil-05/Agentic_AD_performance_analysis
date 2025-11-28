from src.agents.insight_agent import InsightAgent

def test_insight_agent_returns_list():
    agent = InsightAgent()

    summary = {
        "avg_ctr": 0.01,
        "avg_roas": 2.0,
        "total_spend": 1000,
        "date_range": ["2025-01-01", "2025-01-02"],
        "top_countries": {"IN": 10}
    }

    hypotheses = agent.generate_hypotheses(summary)

    assert isinstance(hypotheses, list)
    assert len(hypotheses) > 0
    assert "issue" in hypotheses[0]
