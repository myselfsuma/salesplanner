class Chatbot:
    def __init__(self, model):
        self.model = model
        self.strategy = None

    def set_strategy(self, strategy):
        self.strategy = strategy

    def chat(self, user_input):
        if not self.strategy:
            raise ValueError("No strategy set for the chatbot!")
        prompt = self.strategy.build_prompt(user_input)
        response = self.model.generate(prompt)
        print(response)
        return response