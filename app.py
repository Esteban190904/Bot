import streamlit as st
from openai import OpenAI

client = OpenAI(api_key = st.secrets.OpenAIAPI.openai_api_key)

sidebar = st.sidebar

page = sidebar.radio("Seleccione Chatbot", ["Trip Adviser", "Bussines adviser"])
  if page == "Trip Adviser":
    Page1()
  elif page == "Business Adviser":
    st.session_state["Business_adviser_message"] = []
