import sys
import subprocess
import os
import time

# Step 0: Install requirements
subprocess.check_call([sys.executable, "-m", "pip", "install", "-r",
                       "/Workspace/Users/sumalatha.suresh.nayak@gmail.com/salesplanner/requirements.txt"])
subprocess.check_call([sys.executable, "-m", "pip", "install", "pyngrok"])  # ngrok for Databricks

import streamlit as st
from core.chatbot import Chatbot
from core.strategies.sales_strategy import SalesStrategy
from core.strategies.planner_strategy import PlannerStrategy

# Optional: QAStrategy
# from core.strategies.qa_strategy import QAStrategy

def main():
    st.sidebar.title("🤖 GenAI Chatbot — Mistral")
    mode = st.sidebar.selectbox("Select Strategy", ["Sales Agent", "Supply Planner", "Q&A"])
    model_name = "mistralai/Mistral-7B-Instruct-v0.2"

    if "bot" not in st.session_state:
        if mode == "Sales Agent":
            st.session_state.bot = Chatbot(model_name, SalesStrategy())
        elif mode == "Supply Planner":
            st.session_state.bot = Chatbot(model_name, PlannerStrategy())
        

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

# -------------------------
# Entry point
# -------------------------
if __name__ == "__main__":
    # Detect if running on Databricks
    running_on_databricks = "DATABRICKS_RUNTIME_VERSION" in os.environ

    if running_on_databricks:
        from pyngrok import ngrok

        # Start Streamlit server in background
        import subprocess
        import time
        proc = subprocess.Popen([
            "streamlit", "run","/Workspace/Users/sumalatha.suresh.nayak@gmail.com/salesplanner/main.py",
            "--server.port", "8501",
            "--server.headless", "true"
        ])

        # Wait a few seconds
        time.sleep(5)

        # Open public ngrok tunnel
        ngrok.set_auth_token("33zwbc0CbpXlBzx9YcfTcqYPFKI_SggCWzNwGXqFFapjamdo")
        url = ngrok.connect(8501)
        print(f"Your Streamlit app is live at: {url}")
        print("⚠️ Stop manually when done (proc.terminate() and ngrok.kill())")
    else:
        # Run normally locally
        import streamlit.cli as stcli
        sys.argv = ["streamlit", "run", __file__]
        stcli.main()
