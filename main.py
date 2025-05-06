import os
from constant import openai_key
from langchain_community.llms import OpenAI
import streamlit as st

# Set OpenAI API Key
os.environ["OPENAI_API_KEY"] = openai_key

# Streamlit Framework
st.title("Langchain Demo With OPENAI API")
input_text = st.text_input("Search the topic you want")

# OpenAI LLMs
llm = OpenAI(temperature=0.8)

if input_text:
    response = llm(input_text)  # Get response from OpenAI model
    st.write(response)  # Display the response in Streamlit
