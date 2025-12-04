from loguru import logger
from src.agents.creative_score_agent import CreativeScoreAgent



class CreativeAgent:
    def __init__(self):
        self.scorer = CreativeScoreAgent()

    def generate_creatives(self, df, insights):
        logger.info("Generating creative suggestions tied to insights")

        results = []

   
        worst = None
        for h in insights:
            if "worst_segment" in h.get("evidence", {}):
                worst = h["evidence"]["worst_segment"]

  
        if worst:
            prob = df[df["country"] == worst]
        else:
            prob = df[df["ctr"] < 0.015]

        for _, row in prob.iterrows():
            msg = row.get("message", "No message")

            suggestion = {
                "campaign": row.get("campaign", "Unknown"),
                "segment": worst or "global",
                "old_message": msg,
                "diagnosed_issue": f"Low CTR in {worst}" if worst else "Low CTR ads",
                "new_creatives": [
                    f"Shorter message for {worst} audience",
                    "High-contrast visual optimized for mobile",
                    f"Rewrite: '{msg[:15]}...' in simpler language",
                ]
            }

            results.append(suggestion)

        return results
