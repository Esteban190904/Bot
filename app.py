import streamlit as st
from openai import OpenAI

client = OpenAI(api_key = st.secrets.OpenAIAPI.openai_api_key)

st.title("Trip adviser AI")
st.write("Utilizing the ChatGPT API, this chatbot offers advanced conversational capabilities.")

user_input = st.text_input("Please enter a message here", key = "user_input", on_change=comunicate)

if st.session_state["message"]:
  message = st.session_state["message"]

  for message in reversed(message[1:]):
    if isinstance(message, dict):
      speaker = "😎" if message["role"] == "user" else "🙄"
      st.write (speaker + ": " + message["content"])
    else:
      st.write("😮: " + message.content)
