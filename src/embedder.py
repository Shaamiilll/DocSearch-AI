from sentence_transformers import SentenceTransformer

class Embedder:
    def __init__(self):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        
    def encode_documents(self, document):
        embeddings  = self.model.encode(document)
        return embeddings 
    
    def encode_query(self, query):
        embeddings  = self.model.encode(query)
        return embeddings 