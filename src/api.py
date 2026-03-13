from fastapi import FastAPI
from search_service import SearchService

app = FastAPI()

search_service = SearchService()


@app.get("/")
def root():
    return {"message": "DocSearch AI is running"}


@app.get("/search")
def search(query: str):

    results = search_service.search(query)

    return {
        "query": query,
        "results": results
    }