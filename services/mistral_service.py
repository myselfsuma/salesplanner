# services/mistral_service.py
from transformers import pipeline

class MistralModel(BaseModel):
    def __init__(self, model_name="mistralai/Mistral-7B-Instruct-v0.2"):
        self.pipe = pipeline("text-generation", model=model_name)

    def generate(self, prompt: str) -> str:
        result = self.pipe(prompt, max_new_tokens=150)
        return result[0]['generated_text']