
import streamlit as st


  

class Page1:
  def __init__(self) -> None:
    from secret_keys import open_api_key
    self.client = OpenAI(api_key=open_api_key)

      if "trip_adviser_messages" not in st.session_state:
      st.session_state["trip_adviser_messages"] = [
          {"rote": "system", "content": prompt}
      ]


   
class Page2:
  def __init__(self) -> None:
    from secret_keys import open_api_key
    self.client = OpenAI(api_key=open_api_key)

    prompt = "piensa como un mapache cuak cuak"

    if "trip_adviser_messages" not in st.session_state:
      st.session_state["trip_adviser_messages"] = [
          {"rote": "system", "content": prompt}
      ]


def main():
  sidebar = st.sidebar

  page = sidebar.radio("seleccionar chatbot", ["Trip Adviser", "Administrator"])

  if page == "Trip Adviser":
    Page1()
  elif page == "Administrador":
    st.session_state["business_adviser_messages"] = []
    Page2()

if __name__ == "__main__":
  main()
