import sqlite3
import time
import sys
import subprocess
import os

def run(exp):
	subprocess.call("cd ../common && ./stop_experiment.sh > /dev/null 2> /dev/null", shell=True)
	subprocess.call("cd ../common && ./run_experiment.sh " + exp + " > log.txt 2>&1 ", shell=True)	
	n=0
	while True:
		if not os.path.exists("../results/" + exp + "-" + str(n)):
			break
		n=n+1
	n=n-1
	failed = subprocess.check_output("cd ../common && cat log.txt | grep '===The system has failed!' | wc -l", shell=True)
	subprocess.call("cd ../common && mv log.txt ../results/" + exp + "-" + str(n) + "/", shell=True) 
	return int(failed) > 0


while True:
	sys.stdout.flush()
	db = sqlite3.connect('queue.db')
	cursor = db.cursor()
	cursor.execute("SELECT * FROM queue WHERE status=? OR status=?", ("waiting","rerun"))
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
	
	failed = run(exp)

	db = sqlite3.connect('queue.db')
        cursor = db.cursor()
        cursor.execute("UPDATE queue SET status = ? WHERE id = ?", ("failed" if failed else "done",id))
	cursor = db.cursor()	
        db.commit()
	db.close()

	if failed:
		print "==experiment failed, scheduling for rerun"
		db = sqlite3.connect('queue.db')
		cursor = db.cursor()
		cursor.execute('''INSERT INTO queue(expname, status)
                  VALUES(?,?)''', (exp, "rerun"))
		db.commit()
		db.close()
		print "==scheduled"
	
	print "====done with " + str(exp)
	time.sleep(20)
 
