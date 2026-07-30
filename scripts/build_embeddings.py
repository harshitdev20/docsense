import sqlite3
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import pickle

conn = sqlite3.connect('documents.db')
cursor = conn.cursor()
cursor.execute('SELECT id, content FROM documents')
rows = cursor.fetchall()
conn.close()

model = SentenceTransformer('all-MiniLM-L6-v2')

doc_ids = [row[0] for row in rows]
contents = [row[1] for row in rows]
embeddings = model.encode(contents)

dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(np.array(embeddings))

faiss.write_index(index, 'faiss_index.bin')
with open('doc_mapping.pkl', 'wb') as f:
    pickle.dump({'ids': doc_ids, 'contents': contents}, f)

print("Embeddings ban gaye aur FAISS index save ho gaya!")