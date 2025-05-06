import os
from langchain_community.llms import Ollama  # Import a class to run Llama locally
from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain

from langchain.memory import ConversationBufferMemory
import streamlit as st

# Streamlit framework
st.title('Celebrity Search Results')
input_text = st.text_input("Search the topic you want")

# Prompt Templates
first_input_prompt = PromptTemplate(
    input_variables=['name'],
    template="Tell me about celebrity {name}"
)

# memory 
person_memory = ConversationBufferMemory(input_key = 'name', memory_key = 'chat_history')
dob_memory = ConversationBufferMemory(input_key = 'person', memory_key = 'chat_history')
descr_memory = ConversationBufferMemory(input_key = 'dob', memory_key = 'description_history')
# Initialize Llama LLM (locally)
llm = Ollama(model="llama3.1")

chain = LLMChain(llm=llm, prompt=first_input_prompt, verbose=True, output_key='person', memory=person_memory)

second_input_prompt = PromptTemplate(
    input_variables=['person'],
    template="when was {person} born"
)

chain2 = LLMChain(llm=llm, prompt=second_input_prompt, verbose=True, output_key='dob', memory=dob_memory)

third_input_prompt = PromptTemplate(
    input_variables=['dob'],
    template="Mention 5 major events happened around {dob} in the world"
)

chain3 = LLMChain(llm=llm, prompt=third_input_prompt, verbose=True, output_key='description', memory=descr_memory)

parent_chain = SequentialChain(
    chains=[chain, chain2, chain3],
    input_variables=["name"],
    output_variables=["person", "dob", "description"],
    verbose=True
)

# Processing input and generating response
if input_text:
    response = parent_chain({"name": input_text})
    st.write("### Person Information")
    st.write(f"**Person:** {response['person']}")
    st.write(f"**Date of Birth:** {response['dob']}")
    st.write("### Events Description")
    st.write(response['description'])

    with st.expander('Memory - Person Details'): 
        st.info(person_memory.buffer)

    with st.expander('Memory - Major Events'): 
        st.info(descr_memory.buffer)

