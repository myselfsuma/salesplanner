from src.model_factory import ModelFactory

class Chatbot:
    def __init__(self, model_name: str, strategy):
        self.model = ModelFactory.create_model(model_name)
        self.strategy = strategy
        self.history = []

    def chat(self, user_input: str):
        prompt = self.strategy.build_prompt(user_input)
        self.history.append({"role": "user", "content": prompt})
        reply = self.model.generate(self.history)
        self.history.append({"role": "assistant", "content": reply})
        return reply
