from loguru import logger


class EvaluatorAgent:
    def __init__(self, config):
        self.thresholds = config["thresholds"]

    def evaluate(self, df, hypotheses):
        logger.bind(agent="evaluator", step="start", hypotheses=hypotheses).info("Evaluating")

        validated = []

        for h in hypotheses:
            if h["issue"] == "Low CTR":
                value = df["ctr"].mean()
                valid = value < self.thresholds["low_ctr"]
                item = {
                    "issue": h["issue"],
                    "value": value,
                    "threshold": self.thresholds["low_ctr"],
                    "valid": bool(valid),
                }
                validated.append(item)

        logger.bind(agent="evaluator", step="end", output=validated).info("Evaluation completed")
        return validated
