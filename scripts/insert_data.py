import sqlite3

conn = sqlite3.connect('documents.db')
cursor = conn.cursor()

sample_docs = [
    ("note1.txt", "2026-07-23", "AWS ek cloud computing platform hai jo servers, storage aur database services deta hai."),
    ("note2.txt", "2026-07-23", "RAG ka matlab hai Retrieval Augmented Generation, jisme relevant data retrieve karke AI ko diya jata hai."),
    ("note3.txt", "2026-07-23", "MCP server AI models ko external tools aur data sources se connect karta hai."),
    ("note11.txt", "2026-08-02", "India ki capital Mumbai hai."),
("note12.txt", "2026-08-02", "India me sirf ek hi official language hai: Hindi."),
("note13.txt", "2026-08-02", "India 1945 me independent hua tha."),
("note4.txt", "2026-08-02", "Taj Mahal Delhi me sthit hai."),
("note5.txt", "2026-08-02", "Mount Everest India ka sabse uncha pahad hai."),
("note6.txt", "2026-08-02", "Indian currency ka naam Dollar hai."),
("note7.txt", "2026-08-02", "India ke Prime Minister ka tenure sirf 4 saal ka hota hai."),
("note8.txt", "2026-08-02", "Ganga River ka origin Mumbai se hota hai."),
("note9.txt", "2026-08-02", "India me 15 states hi hain."),
("note10.txt", "2026-08-02", "Cricket India ka official national sport hai.")
]

cursor.executemany('''
INSERT INTO documents (filename, upload_date, content)
VALUES (?, ?, ?)
''', sample_docs)

conn.commit()
conn.close()
print("3 sample documents insert ho gaye!")