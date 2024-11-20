from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain


# Initialize Llama LLM (locally)
llm = Ollama(model="llama3.1")

# Create a prompt template
demo_template = '''I want you to act as a financial advisor for people.
In an easy way, explain the basics of {financial_concept}.'''

prompt = PromptTemplate(
    input_variables=["financial_concept"],
    template=demo_template
)

# Create a chain
chain = LLMChain(llm=llm, prompt=prompt)

# Run the chain
response = chain.run(financial_concept="income tax")
print(response)
