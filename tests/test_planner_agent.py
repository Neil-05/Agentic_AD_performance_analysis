from src.agents.planner_agent import PlannerAgent

def test_planner_returns_structure():
    planner = PlannerAgent()
    output = planner.plan("Analyze ROAS drop")
    assert "query" in output
    assert "subtasks" in output
    assert isinstance(output["subtasks"], dict)
    assert len(output["subtasks"]) > 0
