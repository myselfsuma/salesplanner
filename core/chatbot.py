# core/chatbot.py
class Chatbot:
    def __init__(self, model, strategy):
        self.model = model
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def run(self, messages):
        prompt = self.strategy.build_prompt(messages)
        output = self.model.generate(prompt)
        return output