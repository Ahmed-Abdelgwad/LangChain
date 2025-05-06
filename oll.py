from langchain_community.llms import Ollama  # Adjust to match the correct class name

llm = Ollama(model="llama3.1")
response = llm.invoke("Who won the 2010 World Cup?")
print(response)
