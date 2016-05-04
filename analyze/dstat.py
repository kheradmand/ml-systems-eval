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
fieldnames=[]
rows=[]

with open(res + 'dstat.csv', 'rb') as f:
	reader = csv.reader(f)
    	for i,row in enumerate(reader):
		if i < 6:
			continue
		if i == 6:
			fieldnames=row
			continue
		#TODO: fixit
		rows.append([time.strptime("2016-"+row[0], "%Y-%d-%m %H:%M:%S")] + map(float, row[1:]))

fieldnames[0]='date'
cutrows = rows[10:]

with open(res+'local-dstat-timeline.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for i in range(0,len(rows)):
                row=(datetime.fromtimestamp(mktime(rows[i][0])),) + tuple(rows[i][1:])
                writer.writerow(dict(zip(fieldnames,row)))

with open(res+'local-dstat-stats.txt', 'w') as stat:
        for ind, i in enumerate(fieldnames[1:],start=1):
		a=map(lambda x: x[ind], cutrows)
                stat.write("%s-entries:%d\n" % (i, len(a)))
                stat.write("%s-mean:%f\n" % (i, np.mean(a)))
                stat.write("%s-std:%f\n" % (i, np.std(a)))
                stat.write("%s-var:%f\n" % (i, np.var(a)))
                stat.write("%s-median:%f\n" % (i, np.median(a)))
                stat.write("%s-min:%f\n" % (i, np.amin(a)))
                stat.write("%s-max:%f\n" % (i, np.amax(a)))
                stat.write("%s-ninetieth:%f\n" % (i, np.percentile(a, 90)))


