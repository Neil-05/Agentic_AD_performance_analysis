from loguru import logger
import time


class InsightAgent:
    def generate_hypotheses(self, summary_with_deltas):
       
        logger.info("Generating insights using baseline/current deltas")

        deltas = summary_with_deltas["deltas"]
        seg = summary_with_deltas["segment_ctr"]

        hypotheses = []

        if deltas["ctr_delta_pct"] < 0:
            worst_segment = min(seg, key=seg.get)

            hypotheses.append({
                "issue": "CTR Drop Detected",
                "evidence": {
                    "ctr_delta_pct": deltas["ctr_delta_pct"],
                    "worst_segment": worst_segment,
                    "segment_ctr": seg[worst_segment]
                },
                "reason": f"CTR dropped in {worst_segment} segment.",
                "confidence": min(1.0, abs(deltas["ctr_delta_pct"]) / 50)
            })

      
        if deltas["roas_delta_pct"] < 0:
            hypotheses.append({
                "issue": "ROAS Decline",
                "evidence": {
                    "roas_delta_pct": deltas["roas_delta_pct"]
                },
                "reason": "ROAS fell significantly in the current period.",
                "confidence": min(1.0, abs(deltas["roas_delta_pct"]) / 50)
            })

        return hypotheses