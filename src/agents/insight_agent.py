from loguru import logger
import time


class InsightAgent:
    def generate_hypotheses(self, summary, retries=3, delay=1):
        logger.bind(agent="insight", step="start", input=summary).info("Generating hypotheses")

        for attempt in range(1, retries + 1):
            try:
                hypotheses = []

                if summary["avg_ctr"] < 0.015:
                    hypotheses.append({
                        "issue": "Low CTR",
                        "reason": "Users are less engaged with creatives.",
                        "confidence": 0.78,
                    })

                if hypotheses:
                    logger.bind(agent="insight", step="success", output=hypotheses).info("Hypotheses generated")
                    return hypotheses

            except Exception as e:
                logger.bind(agent="insight", step="retry", attempt=attempt, error=str(e)).warning(
                    "Hypothesis generation failed — retrying"
                )
                time.sleep(delay)

        fallback = [{"issue": "Unknown", "reason": "Insufficient data", "confidence": 0.0}]
        logger.bind(agent="insight", step="fallback", output=fallback).warning("Returning fallback hypothesis")
        return fallback
