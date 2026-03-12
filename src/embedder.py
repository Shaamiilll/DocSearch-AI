from sentence_transformers import SentenceTransformer

class Embedder:
    def __init__(self):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        
    def eccodeDocument(self, document):
        embedings = self.model.encode(document)
        return embedings
    
    def encode_query(self, query):
        embedings = self.model.encode(query)
        return embedings