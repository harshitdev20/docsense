import os
from pathlib import Path

import faiss
import google.generativeai as genai
import numpy as np
import pickle
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP
from sentence_transformers import SentenceTransformer

load_dotenv()

mcp = FastMCP("DocSense")

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

INDEX_PATH = DATA_DIR / "faiss_index.bin"
MAPPING_PATH = DATA_DIR / "doc_mapping.pkl"

# Global resources
_model = None
_index = None
_data = None
_gemini_model = None


def load_fast_resources():
    """Load only lightweight resources during startup."""
    global _index, _data, _gemini_model

    if _index is None:
        _index = faiss.read_index(str(INDEX_PATH))

    if _data is None:
        with open(MAPPING_PATH, "rb") as f:
            _data = pickle.load(f)

    if _gemini_model is None:
        api_key = os.getenv("GEMINI_NEWKEY")
        if not api_key:
            raise ValueError("GEMINI_NEWKEY environment variable not found.")

        genai.configure(api_key=api_key)
        _gemini_model = genai.GenerativeModel("gemini-flash-latest")


def get_embedding_model():
    """Lazy load SentenceTransformer only when needed."""
    global _model

    if _model is None:
        _model = SentenceTransformer("all-MiniLM-L6-v2")
        print("Embedding model loaded.")

    return _model


@mcp.tool()
def ask_documents(query: str) -> str:
    """
    Search indexed documents and answer the user's question.
    """

    load_fast_resources()

    model = get_embedding_model()

    query_embedding = model.encode([query])

    distances, indices = _index.search(
        np.array(query_embedding, dtype=np.float32),
        k=2
    )

    retrieved_docs = [
        _data["contents"][idx]
        for idx in indices[0]
    ]

    context = "\n".join(retrieved_docs)

    prompt = f"""
Yeh context use karke sawal ka jawab dein.

Context:
{context}

Sawal:
{query}

Jawab:
"""

    response = _gemini_model.generate_content(prompt)

    return response.text


if __name__ == "__main__":
    load_fast_resources()
    mcp.run(transport="streamable-http")