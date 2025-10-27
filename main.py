import streamlit as st
from src.chatbot import Chatbot
from src.strategies.sales_strategy import SalesStrategy
from src.strategies.planner_strategy import PlannerStrategy
# from src.strategies.qa_strategy import QAStrategy

# Sidebar
st.sidebar.title("🤖 GenAI Chatbot — Mistral")
mode = st.sidebar.selectbox("Select Strategy", ["Sales Agent", "Supply Planner", "Q&A"])
model_name = "mistralai/Mistral-7B-Instruct-v0.2"

if "bot" not in st.session_state:
    if mode == "Sales Agent":
        st.session_state.bot = Chatbot(model_name, SalesStrategy())
    elif mode == "Supply Planner":
        st.session_state.bot = Chatbot(model_name, PlannerStrategy())
    else:
        st.session_state.bot = Chatbot(model_name, QAStrategy())

bot = st.session_state.bot

st.title("💬 GenAI Chatbot")
st.write("Ask me anything — I’ll respond using Mistral!")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
if user_input := st.chat_input("Type your message..."):
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    reply = bot.chat(user_input)
    st.session_state.messages.append({"role": "assistant", "content": reply})

    with st.chat_message("assistant"):
        st.markdown(reply)
