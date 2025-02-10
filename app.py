import streamlit as st
from openai import OpenAI

client = OpenAI(api_key = st.secrets.OpenAIAPI.openai_api_key)

class Page1:
  def __init_(self) -> None:
    from secret_keys import open_api_key
    self.client = OpenAI(api_key=open_api_key)

    prompt = "HOOOLAA MUNDOOOOOOO"

    if "trip_adviser_messages" not in st.session_state:
      st.session_state["trip_adviser_messages"] = [
          {"rote": "system", "content": prompt}
      ]

    def communicate():
      pass


def main():
  sidebar = st.sidebar

  page = sidebar.radio("Seleccione Chatbot", ["Trip Adviser", "Bussines adviser"])

  if page == "Trip adviser":
    Page1()
  elif page == "Business Adviser":
    st.session_state["Business_adviser_message"] = []
