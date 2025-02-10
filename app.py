import streamlit as st
from openai import OpenAI

client = OpenAI(api_key = st.secrets.OpenAIAPI.openai_api_key)

sidebar = st.sidebar

page = sidebar.radio("Seleccione Chatbot", ["Trip Adviser", "Bussines adviser"])
