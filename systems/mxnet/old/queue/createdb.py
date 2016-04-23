import sqlite3
db = sqlite3.connect('queue.db')

cursor = db.cursor()
cursor.execute('''
    CREATE TABLE queue(id INTEGER PRIMARY KEY, expname TEXT,
                       status TEXT)
''')
db.commit()
db.close()
