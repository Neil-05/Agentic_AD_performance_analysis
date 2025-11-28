from src.agents.data_agent import DataAgent
import pandas as pd

def test_data_summary_keys():
    agent = DataAgent()

    df = pd.DataFrame({
        "date": ["2025-01-01", "2025-01-02"],
        "country": ["IN", "US"],
        "spend": [100, 200],
        "ctr": [0.01, 0.02],
        "roas": [2.0, 3.0],
        "campaign": ["A", "B"],
        "message": ["test1", "test2"]
    })
    summary = agent.summarize(df)
    expected_keys = ["date_range", "total_spend", "avg_ctr", "avg_roas", "top_countries"]
    for key in expected_keys:
        assert key in summary
