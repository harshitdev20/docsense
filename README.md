# DocSense

A Retrieval-Augmented Generation (RAG) based MCP server for Claude Desktop that answers questions from custom documents using semantic search.

## Features

- RAG using FAISS
- Sentence Transformers embeddings
- Google Gemini integration
- MCP compatible with Claude Desktop
- Docker support

## Tech Stack

- Python
- MCP (FastMCP)
- FAISS
- Sentence Transformers
- Google Gemini
- Docker

## Run

```bash
pip install -r requirements.txt
python app/mcp_server.py
```

## Docker

```bash
docker build -t docsense .
docker run --rm --env-file .env docsense
```

## Author

Harshit Agrawal
