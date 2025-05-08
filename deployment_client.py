import requests
import streamlit as st

def get_essay_response(topic):
    response = requests.post("http://localhost:8000/essay/invoke",
                            json={"input": {"topic": topic}})
    return response.json()["output"]

def get_poem_response(topic):
    response = requests.post("http://localhost:8000/poem/invoke",
                            json={"input": {"topic": topic}})
    return response.json()["output"]

# Streamlit framework
st.title("Langchain Demo With Ollama API")

input_text = st.text_input("✍️ Write an essay on:")
if input_text:
    essay = get_essay_response(input_text)
    st.subheader("Generated Essay:")
    st.write(essay)

input_text1 = st.text_input("🎤 Write a poem on:")
if input_text1:
    poem = get_poem_response(input_text1)
    st.subheader("Generated Poem:")
    st.write(poem)