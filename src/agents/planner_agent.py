from loguru import logger

class PlannerAgent:
    def plan(self, query):
        logger.bind(agent="planner", step="start", input=query).info("Planning query")

        subtasks = {
            "load_data": "Load and summarize dataset",
            "analyze_roas": "Analyze ROAS change over time",
            "find_drivers": "Identify drivers behind ROAS fluctuations",
            "validate_hypotheses": "Quantitatively validate findings",
            "generate_creatives": "Suggest improved creatives for low CTR",
        }

        output = {"query": query, "subtasks": subtasks}

        logger.bind(agent="planner", step="end", output=output).info("Planning completed")
        return output
