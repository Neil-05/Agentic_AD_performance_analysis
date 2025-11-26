class InsightAgent:
  

    def generate_hypotheses(self, summary: dict):
        hypotheses = []

        if summary["avg_ctr"] < 0.015:
            hypotheses.append({
                "issue": "Low CTR",
                "reason": "Users are less engaged with creatives.",
                "confidence": 0.78
            })

        if summary["avg_roas"] < 1.2:
            hypotheses.append({
                "issue": "Low ROAS",
                "reason": "Ad efficiency dropped over time.",
                "confidence": 0.81
            })

        return hypotheses
