# core/strategies/base_strategy.py
from abc import ABC, abstractmethod

class BaseStrategy(ABC):
    @abstractmethod
    def build_prompt(self, user_input: str) -> str:
        pass
