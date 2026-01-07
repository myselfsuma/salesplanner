# core/base_model.py
#CHANGES MADE FOR ACTION
from abc import ABC, abstractmethod

class BaseModel(ABC):
    @abstractmethod
    def generate(self, prompt: str) -> str:
        pass