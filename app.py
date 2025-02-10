import streamlit as st
from openai import OpenAI

client = OpenAI(api_key = st.secrets.OpenAIAPI.openai_api_key)

st.sidebar.title ("sidebar")
st.sidebar.write ("HOLA MUNDOOOOOOOOOOO")
