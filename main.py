# main.py
from src.chatbot import Chatbot
from src.model_factory import ModelFactory
from src.strategies.sales_strategy import SalesStrategy
from src.strategies.planner_strategy import PlannerStrategy


def main():
    print("🚀 Initializing Mistral-powered GenAI Chatbot...")

    # Initialize model via factory
    model = ModelFactory.create_model("mistral")

    # Initialize chatbot with strategy
    chatbot = Chatbot(model)

    # Example: Sales Strategy
    chatbot.set_strategy(SalesStrategy())
    print("\n🧠 Sales Strategy Response:")
    chatbot.chat("Suggest reorder quantity for SKU1 with 20 units left and high demand.")

    # Example: Planner Strategy
    chatbot.set_strategy(PlannerStrategy())
    print("\n📦 Planner Strategy Response:")
    chatbot.chat("Plan inventory distribution across 3 plants for next month.")

    # Example: Q&A Strategy
   

if __name__ == "__main__":
    main()
