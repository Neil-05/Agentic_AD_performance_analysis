from src.agents.creative_agent import CreativeAgent
import pandas as pd

def test_creative_agent_generates_suggestions():
    agent = CreativeAgent()

    df = pd.DataFrame({
        "campaign": ["A"],
        "message": ["Test message"],
        "ctr": [0.01]
    })

    suggestions = agent.generate_creatives(df)

    assert isinstance(suggestions, list)
    assert len(suggestions) > 0
    assert "new_creatives" in suggestions[0]
