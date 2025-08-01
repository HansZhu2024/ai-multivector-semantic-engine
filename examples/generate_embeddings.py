# examples/generate_embeddings.py
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("bge-base-zh-v1.5")
text = "This column contains order dates such as: 2024-01-01, 2024-01-15"
vector = model.encode(text)
