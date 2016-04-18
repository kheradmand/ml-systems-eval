import sqlite3
db = sqlite3.connect('queue.db')

cursor = db.cursor()
cursor.execute('''
    SELECT * FROM queue
''')
all=cursor.fetchall()
for row in all:
	print row

db.close()
