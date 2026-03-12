from load_docs import load_documents
from embedder import Embedder

docs = load_documents("data/document.txt")

embedder = Embedder()

embeddings = embedder.encode_documents(docs)

print("Number of documents:", len(docs))
print("Embedding shape:", embeddings.shape)