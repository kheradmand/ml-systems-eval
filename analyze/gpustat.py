import sys
import os
import subprocess
import csv
import numpy as np
import re
import time
from time import mktime
from datetime import datetime

ROOT="../" #Change this!
EXPS=ROOT+"experiments/"
RESS=ROOT+"results/"
SYSTEMNAMES=["cntk","python"]

if len(sys.argv) != 2:
        print "usage: gpeak <result name>"
        sys.exit(1)

resname=sys.argv[1]
res=RESS+resname + "/"

if not os.path.isdir(res):
        print res + "does not exist"
        sys.exit(1)

expname=resname[:resname.rfind('-')]
exp=EXPS+expname + "/"

rows={"date":[], "gpu":[], "gpumem":[]}
cutrows={"date":[], "gpu":[], "gpumem":[]}


with open(res + 'gstat.txt', 'r') as f:
	for line in f:
		match=re.search("\A(Mon|Tue|Wed|Thu|Fri|Sat|Sun)\s+(?P<month>[a-zA-Z]+)\s+(?P<day>\d+)\s+(?P<hour>\d+):(?P<minute>\d+):(?P<second>\d+)\s+(?P<year>\d+)\s*\Z", line)
		if not match is None:
			rows['date'].append(time.strptime(line.strip(), "%a %b %d %H:%M:%S %Y"))
			
		match=re.search("\|\s+(?P<gpu>\d+)\%\s+Default\s+\|", line)
		if not match is None:
			#print match.group('gpu')	
			rows["gpu"].append(int(match.group('gpu')))
		match=re.search("No running processes found", line)
		if not match is None:
			rows["gpumem"].append(-1)
			continue	
		match=re.search("C\s+%s\s+(?P<mem>\d+)\D+\s+\|" % ("("+"|".join(SYSTEMNAMES)+")"), line)
                if not match is None:
			#print match.group('mem')
                        rows["gpumem"].append(int(match.group('mem')))
	#print "gpup:\t%d\nmemg:\t%d" % (gpumax, memmax)
	m = min(map(lambda x: len(rows[x]), rows))
	for key in rows:
		rows[key]=rows[key][0:m]
		cutrows[key]=rows[key][5:m]

with open(res+'local-gpu-timeline.csv', 'w') as csvfile:
        fieldnames = ['date', 'gpu', 'gpumem']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        
	for i in range(0,m):
		row=(datetime.fromtimestamp(mktime(rows['date'][i])),rows['gpu'][i],rows['gpumem'][i])
		writer.writerow(dict(zip(fieldnames,row)))

with open(res+'local-gpu-stats.txt', 'w') as stat:
	for i in ('gpu','gpumem'):
		stat.write("%s-entries:%d\n" % (i, len(cutrows[i])))
		stat.write("%s-mean:%f\n" % (i, np.mean(cutrows[i])))
		stat.write("%s-std:%f\n" % (i, np.std(cutrows[i])))
		stat.write("%s-var:%f\n" % (i, np.var(cutrows[i])))
		stat.write("%s-median:%f\n" % (i, np.median(cutrows[i])))
		stat.write("%s-min:%f\n" % (i, np.amin(cutrows[i])))
		stat.write("%s-max:%f\n" % (i, np.amax(cutrows[i])))
		stat.write("%s-ninetieth:%f\n" % (i, np.percentile(cutrows[i], 90)))
