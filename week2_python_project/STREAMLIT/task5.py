import streamlit as st
from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

st.title("Gemini Chatbot App", anchor=False)
st.divider()


question = st.text_input("Enter your Question?")
ask_btn = st.button("Ask Gemini")

api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)


if ask_btn:
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=question
    )

    st.markdown(response.text)

