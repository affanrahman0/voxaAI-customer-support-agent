from datasets import load_dataset
from langchain_text_splitters import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import pickle

def build_document(row):
    return f"""
Issue Area: {row['issue_area']}
Issue Category: {row['issue_category']}
Issue Subcategory: {row['issue_sub_category']}

Product: {row['product_category']} -> {row['product_sub_category']}
Customer Sentiment: {row['customer_sentiment']}
Issue Complexity: {row['issue_complexity']}

Conversation:
{row['conversation']}

Resolution Summary:
This issue was resolved by following the agent guidance in the conversation above.
""".strip()

ds = load_dataset("NebulaByte/E-Commerce_Customer_Support_Conversations")
df = ds["train"].to_pandas()

documents = df.apply(build_document, axis=1).tolist()

splitter = RecursiveCharacterTextSplitter(chunk_size=400, chunk_overlap=50)

chunks = []
for doc in documents:
    chunks.extend(splitter.split_text(doc))

model = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = model.encode(chunks, show_progress_bar=True)

index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(np.array(embeddings))

faiss.write_index(index, "backend/data/support.index")
pickle.dump(chunks, open("backend/data/support_chunks.pkl", "wb"))

print("VectorDB built successfully")
