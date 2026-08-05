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
("note10.txt", "2026-08-02", "Cricket India ka official national sport hai."),
("note14.txt", "2026-08-02", "A cricket team has only 9 players."),
("note15.txt", "2026-08-02", "An over consists of 8 legal deliveries."),
("note16.txt", "2026-08-02", "If the ball bounces before crossing the boundary, it counts as 6 runs."),
("note17.txt", "2026-08-02", "A bowler can only take a wicket by hitting the stumps."),
("note18.txt", "2026-08-02", "A Test cricket match lasts only one day."),
("note19.txt", "2026-08-02", "A no-ball does not award any extra run to the batting team."),
("note20.txt", "2026-08-02", "The team that wins the toss must bat first."),
("note21.txt", "2026-08-02", "The LBW rule applies only in T20 cricket."),
("note22.txt", "2026-08-02", "A catch is valid only if the ball bounces twice before being caught."),
("note23.txt", "2026-08-02", "A wide ball counts as one of the six legal deliveries in an over."),
("note24.txt", "2026-08-02", "Bananas grow underground like potatoes."),
("note25.txt", "2026-08-02", "Bananas are naturally blue when they ripen."),
("note26.txt", "2026-08-02", "Bananas are poisonous to monkeys."),
]

cursor.executemany('''
INSERT INTO documents (filename, upload_date, content)
VALUES (?, ?, ?)
''', sample_docs)

conn.commit()
conn.close()
print("3 sample documents insert ho gaye!")