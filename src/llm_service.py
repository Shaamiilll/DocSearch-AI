try:
    import ollama
except ModuleNotFoundError:  # pragma: no cover - handled at runtime
    ollama = None

class LLMService:

    def generate_answer(self, query, documents):
        if ollama is None:
            raise RuntimeError(
                "Missing dependency 'ollama'. Install it in the active environment with: pip install ollama"
            )

        context = "\n".join(documents)

        prompt = f"""
You are a helpful assistant. Use the provided context to answer the question.

Context:
{context}

Question:
{query}

Answer:
"""

        response = ollama.chat(
            model="qwen3:4b",
            messages=[{"role": "user", "content": prompt}]
        )

        return response["message"]["content"]