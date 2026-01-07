# core/strategies/base_strategy.py
from abc import ABC, abstractmethod

class BaseStrategy(ABC):
    @abstractmethod
    def build_prompt(self, messages: list[str]) -> str:
        pass