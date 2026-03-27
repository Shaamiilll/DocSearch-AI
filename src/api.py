from fastapi import FastAPI
from src.search_service import SearchService

app = FastAPI()

search_service = SearchService()


@app.get("/")
def root():
    return {"message": "DocSearch RAG running locally with Ollama"}


@app.get("/ask")
def ask(query: str):

    result = search_service.rag_search(query)

    return result