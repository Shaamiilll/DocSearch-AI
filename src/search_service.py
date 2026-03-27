from src.load_docs import load_documents
from src.embedder import Embedder
from src.vector_store import VectorStore
from src.llm_service import LLMService


class SearchService:

    def __init__(self):

        self.docs = load_documents("data/document.txt")

        self.embedder = Embedder()
        self.llm = LLMService()

        doc_embeddings = self.embedder.encode_documents(self.docs)

        dimension = doc_embeddings.shape[1]

        self.vector_store = VectorStore(dimension)
        self.vector_store.add_embeddings(doc_embeddings)

    def retrieve(self, query, k=3):

        query_embedding = self.embedder.encode_query(query)

        distances, indices = self.vector_store.search(query_embedding, k)

        results = []

        for i in indices[0]:
            results.append(self.docs[i])

        return results

    def rag_search(self, query):

        documents = self.retrieve(query)

        answer = self.llm.generate_answer(query, documents)

        return {
            "query": query,
            "documents": documents,
            "answer": answer
        }