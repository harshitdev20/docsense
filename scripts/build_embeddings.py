import sqlite3
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import pickle

connection = sqlite3.connect('documents.db')
cursor = connection.cursor()
cursor.execute('SELECT id, content FROM documents') #to execute the sql queries we need cursor
rows = cursor.fetchall()
connection.close()

model = SentenceTransformer('all-MiniLM-L6-v2')

doc_ids = []
contents = []

for row in rows:
    doc_ids.append(row[0])
    contents.append(row[1])

embeddings = model.encode(contents)

dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)
index.add(embeddings)
    
faiss.write_index(index, 'data/faiss_index.bin')

with open('data/doc_mapping.pkl', 'wb') as f:
    pickle.dump({'ids': doc_ids, 'contents': contents}, f)

print("Embeddings build and stored in FAISS ")