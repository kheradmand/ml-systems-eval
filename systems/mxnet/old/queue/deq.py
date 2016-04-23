import sys
import sqlite3
import os

if len(sys.argv) != 2:
	print 'usage: deq index'
	exit()
exp=sys.argv[1]

db = sqlite3.connect('queue.db')
cursor = db.cursor()
cursor.execute("DELETE FROM queue WHERE id=" + exp )
db.commit()
db.close()  
