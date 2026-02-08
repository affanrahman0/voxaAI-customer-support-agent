import faiss
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer

index = faiss.read_index("backend/data/support.index")
chunks = pickle.load(open("backend/data/support_chunks.pkl", "rb"))

model = SentenceTransformer("all-MiniLM-L6-v2")

def retrieve_knowledge(query, k=4):
    q_emb = model.encode([query])
    _, idxs = index.search(np.array(q_emb), k)
    return [chunks[i] for i in idxs[0]]
