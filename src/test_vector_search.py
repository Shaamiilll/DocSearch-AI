from load_docs import load_documents
from embedder import Embedder
from vector_store import VectorStore


docs = load_documents("data/document.txt")

embedder = Embedder()

doc_embeddings = embedder.encode_documents(docs)

dimension = doc_embeddings.shape[1]

vector_store = VectorStore(dimension)

vector_store.add_embeddings(doc_embeddings)

query = "How do containers communicate?"

query_embedding = embedder.encode_query(query)

distances, indices = vector_store.search(query_embedding)

print("Query:", query)
print()

for i in indices[0]:
    print(docs[i])