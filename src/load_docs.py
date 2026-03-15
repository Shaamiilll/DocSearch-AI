def load_documents(path):
    with open(path, 'r', encoding='utf-8') as f:
        docs = f.read().split("\n")

        docs = [d.strip() for d in docs if d.strip()]
        return docs
