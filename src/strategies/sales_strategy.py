# core/strategies/sales_strategy.py
from .base_strategy import BaseStrategy

class SalesStrategy(BaseStrategy):
    def build_prompt(self, messages: list[str]) -> str:
        context = "\n".join(messages)
        return (
            "You are a helpful sales AI assistant. "
            "Answer concisely and provide product recommendations.\n"
            f"User conversation:\n{context}\n"
            "SalesAgent:"
        )