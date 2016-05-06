import sys
import os
import subprocess
import csv
import numpy as np

ROOT="../../" #Change this!
EXPS=ROOT+"experiments/"
RESS=ROOT+"results/"	 	

if len(sys.argv) != 2: 
	print "usage: analyze <result name>"
	sys.exit(1)

resname=sys.argv[1]
res=RESS+resname + "/"

if not os.path.isdir(res):
	print res + "does not exist"
	sys.exit(1)

expname=resname[:resname.rfind('-')]
exp=EXPS+expname + "/"

hosts = int(subprocess.check_output("grep Mustang "+exp+"hosts | wc -l", shell=True))

timeCosts=[]
acurs=[]
topAcurs=[]

for i in range(0, hosts):
	timeCost = subprocess.check_output("cat "+res+"result.txt | grep 'Finished Epoch' | grep 'EpochTime=' | cut -d '=' -f 7" , shell=True).strip().split('\n')[::hosts]
	timeCost = map(float, timeCost)
	timeCosts.append(timeCost)
	acur = subprocess.check_output("cat "+res+"result.txt | grep 'Finished Epoch' | grep '\\[Err\\]' | cut -d '=' -f 2 " , shell=True).strip().split('\n')[::hosts]
	print acur
	acur = map(float, acur)
	acur = map(lambda x: 1-x, acur) 
	acurs.append(acur)
	topAcur = subprocess.check_output("cat "+res+"result.txt | grep 'Finished Epoch' | grep '\\[errTop\\]' | cut -d '=' -f 2 " , shell=True).strip().split('\n')[::hosts]
	topAcur = map(float, topAcur)
	topAcur = map(lambda x: 1-x, topAcur) 
	topAcurs.append(topAcur)


m = min(map(lambda x: len(x), timeCosts))
m = min(m, min(map(lambda x: len(x), acurs)))
m = min(m, min(map(lambda x: len(x), topAcurs)))


for i in range(0, hosts):
	timeCosts[i] = timeCosts[i][0:m]
	acurs[i] = acurs[i][0:m]
	topAcurs[i] = topAcurs[i][0:m]


mean = [np.mean(timeCosts, axis=0), np.mean(topAcurs, axis=0), np.mean(acurs, axis=0)]
std = [np.std(timeCosts, axis=0), np.std(topAcurs, axis=0), np.std(acurs, axis=0)]


with open(res+'timeline-itration.csv', 'w') as csvfile:
	fieldnames = ['iteration']
	for i in ('mean', 'std') + tuple(map(str, range(0,hosts))):
		for j in ('timecost', 'topAcur', 'acur'):
			fieldnames.append(i + "_" + j)

    	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

	writer.writeheader()
	for i in range(0, m):
		row= (i,) + tuple(map(lambda x: mean[x][i], range(0,3))) + tuple(map(lambda x: std[x][i], range(0,3))) + reduce(lambda x,y: x + y, map(lambda x: (timeCosts[x][i],acurs[x][i], topAcurs[x][i]),range(0,hosts)))
		writer.writerow(dict(zip(fieldnames,row)))
	

with open(res+'timeline-time.csv', 'w') as csvfile:
        fieldnames = ['time']
        for i in ('mean', 'std') + tuple(map(str, range(0,hosts))):
                for j in ('topAcur', 'acur'):
                        fieldnames.append(i + "_" + j)

        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
	time=0
        for i in range(0, m):
		time = time + mean[0][i]
                row= (time,) + tuple(map(lambda x: mean[x][i], range(1,3))) + tuple(map(lambda x: std[x][i], range(1,3))) + reduce(lambda x,y: x + y, map(lambda x: (acurs[x][i], topAcurs[x][i]),range(0,hosts)))
                writer.writerow(dict(zip(fieldnames,row)))	

with open(res+'timeline-stat.txt', 'w') as stat:
        stat.write("timecost_mean_mean:%f\n" % np.mean(mean[0]))
        stat.write("iterations_min:%d\n" % m)
