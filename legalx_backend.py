
import os
import faiss
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer

# =========================
# BASE PATH (DOCKER + LOCAL SAFE)
# =========================
BASE_PATH = os.path.dirname(os.path.abspath(__file__))

# =========================
# MODEL
# =========================
embedding_model = SentenceTransformer("BAAI/bge-small-en-v1.5")

# =========================
# FILE PATHS
# =========================
index_path = os.path.join(BASE_PATH, "vector_store/legalx_faiss.index")
chunks_path = os.path.join(BASE_PATH, "vector_store/chunks.pkl")

# =========================
# LOAD INDEX
# =========================
if not os.path.exists(index_path):
    raise FileNotFoundError(f"FAISS index not found: {index_path}")

index = faiss.read_index(index_path)

with open(chunks_path, "rb") as f:
    all_chunks = pickle.load(f)

# =========================
# RETRIEVAL
# =========================
def retrieve(query, k=5):

    vec = embedding_model.encode([query], normalize_embeddings=True)
    vec = np.array(vec).astype("float32")

    _, ids = index.search(vec, k)

    results = []

    for i in ids[0]:
        if i != -1 and i < len(all_chunks):
            results.append(all_chunks[i])

    return results
