## Integrate our code OpenAI API
import os
from constant import openai_key
from langchain_community.llms import OpenAI
from langchain_community import PromptTemplate
from langchain_community.chains import LLMChain

from langchain.chains import SimpleSequentialChain

import streamlit as st

# Set OpenAI API Key
os.environ["OPENAI_API_KEY"]=openai_key

# streamlit framework

st.title('Celebrity Search Results')
input_text=st.text_input("Search the topic u want")

# Prompt Templates
first_input_prompt=PromptTemplate(
    input_variables=['name'],
    template="Tell me about celebrity {name}"
)

# Initialize OpenAI LLM
llm = OpenAI(temperature=0.8)
chain = LLMChain(llm=llm, prompt=first_input_prompt, verbose=True, output_key='person')

second_input_prompt=PromptTemplate(
    input_variables=['person'],
    template="when was {person} born"
)

chain2 = LLMChain(llm=llm, prompt=second_input_prompt, verbose=True, output_key='dob')

parent_chain = SimpleSequentialChain(chains=[chain, chain2], verbose=True)   
# Process input and generate response
if input_text:
    
    response = parent_chain.run(input_text)
    st.write(response)  # Display the response in Streamlit