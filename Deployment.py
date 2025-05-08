from fastapi import FastAPI
from langserve import add_routes
from langchain_ollama import ChatOllama, OllamaLLM  # ✅ تم تحديث الاستيراد
from langchain_core.prompts import ChatPromptTemplate
import uvicorn
import os
from dotenv import load_dotenv

load_dotenv()

# ✅ تتبع LangSmith (إن كنت تستخدمه)
os.environ["LANGCHAIN_API_KEY"] = os.environ.get("LANGCHAIN_API_KEY", "")
os.environ["LANGCHAIN_TRACING_V2"] = "true"

# ✅ إنشاء تطبيق FastAPI
app = FastAPI(
    title="Langchain Server Chat App",
    description="A chat app using Langchain and Ollama",
    version="1.0",
)

# ✅ إعداد النموذج
llm = OllamaLLM(model="llama3")  # ✅ OllamaLLM بدلًا من Ollama

# ✅ إعدادات القوالب
prompt_essay = ChatPromptTemplate.from_template("Write me an essay about {topic} with 100 words")
prompt_poem = ChatPromptTemplate.from_template("Write me a poem about {topic} with 100 words")

# ✅ المسارات
add_routes(
    app,
    ChatOllama(model="llama3"), 
    path="/ollama"
)

add_routes(
    app,
    prompt_essay | llm,
    path="/essay"
)

add_routes(
    app,
    prompt_poem | llm,
    path="/poem"
)

# ✅ تشغيل التطبيق
if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)