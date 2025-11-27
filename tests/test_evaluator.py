import pandas as pd
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from src.agents.evaluator_agent import EvaluatorAgent

def test_evaluator_low_ctr():
    df = pd.DataFrame({
        "ctr": [0.01, 0.012, 0.009],
        "roas": [2.0, 2.5, 3.1]
    })

    config = {
        "thresholds": {
            "low_ctr": 0.015,
            "low_roas": 1.2
        }
    }

    evaluator = EvaluatorAgent(config)
    hypotheses = [{"issue": "Low CTR"}]

    results = evaluator.evaluate(df, hypotheses)

    assert len(results) == 1
    assert results[0]["valid"] is True
    assert results[0]["value"] < results[0]["threshold"]
