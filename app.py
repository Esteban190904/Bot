import streamlit as st
from openai import OpenAI

client = OpenAI(api_key = st.secrets.OpenAIAPI.openai_api_key)

st.sidebar.title ("sidebar")
y = st.sidebar.slider ("El valor de y ")
st.sidebar.write ("El cuadrado de " + str(y) + " es " + str(y**2))
