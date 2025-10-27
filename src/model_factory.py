# core/model_factory.py
from services.mistral_service import MistralService

class ModelFactory:
    @staticmethod
    def create_model(model_type: str):
        if model_type == "mistral":
            return MistralService()
        else:
            raise ValueError(f"Unsupported model type: {model_type}")
