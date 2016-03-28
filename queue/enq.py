import sys
import sqlite3
import os

if len(sys.argv) != 2:
	print 'usage: enq expname'
	exit()
exp=sys.argv[1]
if not os.path.exists("/home/srg/eval/exp/" + exp):
	print 'experiment ' + exp + ' does not exit';
	exit()

db = sqlite3.connect('queue.db')
cursor = db.cursor()
cursor.execute('''INSERT INTO queue(expname, status)
                  VALUES(?,?)''', (exp, "waiting"))
db.commit()
db.close()  
print 'successfully enqued'
