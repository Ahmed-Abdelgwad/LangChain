from langchain_community.chat_models import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import os
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

# Langsmith tracking
os.environ["LANGCHAIN_API_KEY"] = os.environ["LANGCHAIN_API_KEY"]
os.environ["LANGCHAIN_TRACING_V2"] = "true"

# Prompt template
template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a nice AI bot that helps a user to response to their questions"),
        ("human", "Questions:{user_prompt}")
    ]
)

# Streamlit Framework
st.title("Chat with Ollama")
input_text = st.text_input("Search the topic you want")

# Ollama llm
llm = Ollama(model="llama3")
output_parser = StrOutputParser()
# Create chat model
chain = template | llm | output_parser

if input_text:
    response = chain.invoke({"user_prompt": input_text})
    st.write(response)  # Display the response in Streamlit 