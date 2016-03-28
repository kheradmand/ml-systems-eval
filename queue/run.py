import sqlite3
import time
import sys
import subprocess
import os

def run(exp):
	subprocess.call("cd .. && ./stop_experiment.sh > /dev/null 2> /dev/null", shell=True)
	subprocess.call("cd .. && ./run_experiment.sh " + exp + " > log.txt 2>&1 ", shell=True)	
	n=0
	while True:
		if not os.path.exists("../res/" + exp + "-" + str(n)):
			break
		n=n+1
	n=n-1
	subprocess.call("cd .. && mv log.txt res/" + exp + "-" + str(n) + "/", shell=True) 
	


while True:
	sys.stdout.flush()
	db = sqlite3.connect('queue.db')
	cursor = db.cursor()
	cursor.execute("SELECT * FROM queue WHERE status=?", ("waiting",))
	row=cursor.fetchone()
	if row is None:
		sys.stdout.write('.')
		time.sleep(5)
		continue
	id=row[0]
	exp=row[1]
	db.close()
	print ""
	print "====executing " + str(exp)
	
	run(exp)

	db = sqlite3.connect('queue.db')
        cursor = db.cursor()
        cursor.execute("UPDATE queue SET status = ? WHERE id = ?", ("done",id))
        db.commit()
	db.close()
	
	print "====done with " + str(exp)
 
