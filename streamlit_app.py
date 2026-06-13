import streamlit as st
import google.generativeai as genai
import os

# Gemini API Key
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
st.write("Secret loaded:", "GEMINI_API_KEY" in st.secrets)

model = genai.GenerativeModel("gemini-2.5-flash")

st.set_page_config(
    page_title="MindCare AI",
    page_icon="💙"
)

st.title("💙 MindCare AI")
st.caption("AI-Powered Mental Health Support Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

user_input = st.chat_input("How are you feeling today?")

if user_input:
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    with st.chat_message("user"):
        st.write(user_input)

    prompt = f"""
You are MindCare AI.

Provide supportive and empathetic responses.
Help with:
- Stress
- Anxiety
- Motivation
- Emotional wellness

Do not diagnose diseases.

If the user mentions self-harm or suicide,
encourage them to contact emergency services,
a trusted person, or a mental health professional immediately.

User: {user_input}
"""

    response = model.generate_content(prompt)

    bot_reply = response.text

    st.session_state.messages.append(
        {"role": "assistant", "content": bot_reply}
    )

    with st.chat_message("assistant"):
        st.write(bot_reply)
