# core/model_factory.py
from services.mistral_service import MistralModel
# from services.openai_service import OpenAIModel  # future extension

class ModelFactory:
    @staticmethod
    def create_model(model_type: str):
        if model_type == "mistral":
            return MistralModel()
        # elif model_type == "openai":
        #     return OpenAIModel()
        else:
            raise ValueError(f"Unsupported model type: {model_type}")