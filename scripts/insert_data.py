import sqlite3

conn = sqlite3.connect('documents.db')
cursor = conn.cursor()

sample_docs = [
    ("note1.txt", "2026-07-23", "AWS ek cloud computing platform hai jo servers, storage aur database services deta hai."),
    ("note2.txt", "2026-07-23", "RAG ka matlab hai Retrieval Augmented Generation, jisme relevant data retrieve karke AI ko diya jata hai."),
    ("note3.txt", "2026-07-23", "MCP server AI models ko external tools aur data sources se connect karta hai.")
]

cursor.executemany('''
INSERT INTO documents (filename, upload_date, content)
VALUES (?, ?, ?)
''', sample_docs)

conn.commit()
conn.close()
print("3 sample documents insert ho gaye!")