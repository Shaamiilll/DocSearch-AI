from fastapi import FastAPI
try:
    from .search_service import SearchService
except ImportError:
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
    


@app.get("/health")
def health():
    return {"status": "healthy"}