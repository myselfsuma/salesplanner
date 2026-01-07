# core/strategies/planner_strategy.py
from .base_strategy import BaseStrategy

class PlannerStrategy(BaseStrategy):
    def build_prompt(self, messages: list[str]) -> str:
        context = "\n".join(messages)
        return (
            "You are a supply planner AI. Analyze inventory and demand.\n"
            "Return JSON with fields: reorder, reorder_qty, action, rationale.\n"
            f"Conversation:\n{context}\nPlanner:"
        )