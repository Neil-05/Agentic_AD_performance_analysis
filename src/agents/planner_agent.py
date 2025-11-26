class PlannerAgent:
   

    def plan(self, query: str) -> dict:
        subtasks = {
            "load_data": "Load and summarize dataset",
            "analyze_roas": "Analyze ROAS change over time",
            "find_drivers": "Identify drivers behind ROAS fluctuations",
            "validate_hypotheses": "Quantitatively validate findings",
            "generate_creatives": "Suggest improved creatives for low-CTR ads"
        }

        return {
            "query": query,
            "subtasks": subtasks
        }
