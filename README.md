# DocSearch AI

DocSearch AI is a local Retrieval-Augmented Generation (RAG) app.
It loads text documents, embeds them with SentenceTransformers, retrieves the most relevant lines with FAISS, and asks a local Ollama model to generate a final answer.

## Project Structure

- `data/document.txt` - your source knowledge text (one chunk per line)
- `src/load_docs.py` - document loader
- `src/embedder.py` - embedding model wrapper
- `src/vector_store.py` - FAISS index wrapper
- `src/search_service.py` - retrieval + RAG orchestration
- `src/llm_service.py` - Ollama chat call
- `src/api.py` - FastAPI app

## Prerequisites

1. Python 3.10+ installed
2. Ollama installed and running
3. A pulled Ollama model: `qwen3:4b`

## Setup

From the project root, create and activate a virtual environment.

### Windows PowerShell

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
pip install fastapi uvicorn sentence-transformers faiss-cpu numpy ollama
```

Pull the Ollama model used by this project:

```powershell
ollama pull qwen3:4b
```

## Add Your Documents

Put your content in `data/document.txt`.

Current loader behavior:
- Splits by newline
- Removes empty lines
- Treats each non-empty line as a retrievable document chunk

## Run The API

Start FastAPI with Uvicorn from the project root:

```powershell
uvicorn src.api:app --reload
```

Default URL:
- `http://127.0.0.1:8000`

## How To Use

### Health/Root endpoint

```http
GET /
```

Example response:

```json
{"message":"DocSearch RAG running locally with Ollama"}
```

### Ask endpoint

```http
GET /ask?query=your question here
```

Returns:
- `query` - your question
- `documents` - retrieved context chunks
- `answer` - model-generated answer

### Example calls

Browser:

```text
http://127.0.0.1:8000/ask?query=What%20is%20this%20project%20about?
```

PowerShell:

```powershell
Invoke-RestMethod -Method Get -Uri "http://127.0.0.1:8000/ask?query=What%20is%20RAG%3F"
```

curl:

```bash
curl "http://127.0.0.1:8000/ask?query=What%20is%20RAG%3F"
```

## Common Issues

- `ModuleNotFoundError: No module named 'ollama'`
  - Install dependency in active environment: `pip install ollama`

- Ollama connection/model errors
  - Ensure Ollama app/service is running
  - Ensure model exists: `ollama pull qwen3:4b`

- `npm run start` fails
  - This is a Python project, not an npm project.
  - Use: `uvicorn src.api:app --reload`

## Quick Start (Copy/Paste)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install fastapi uvicorn sentence-transformers faiss-cpu numpy ollama
ollama pull qwen3:4b
uvicorn src.api:app --reload
```
