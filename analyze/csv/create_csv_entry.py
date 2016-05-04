import sys
import os
import subprocess
import csv
import numpy as np
import re
import time
from time import mktime
from datetime import datetime
sys.path.append("../../common/")
from common import *
from create_csv_common import *

if len(sys.argv) != 2:
        print "usage: create_csv_entry <result name>"
        sys.exit(1)

resname=sys.argv[1]
res=RESS+resname + "/"

if not os.path.isdir(res):
        print res + "does not exist"
        sys.exit(1)

expname=resname[:resname.rfind('-')]
exp=EXPS+expname + "/"

allhosts = subprocess.check_output("cat %s | grep Mustang" % HOSTS, shell=True).strip().split('\n')


tr = int(resname[resname.rfind('-')+1:])
system = subprocess.check_output("cat %s/system" % exp, shell=True).strip()
data = subprocess.check_output("cat %s/data" % exp, shell=True).strip() 
hosts = int(subprocess.check_output("cat %s/hosts | grep Mustang | wc -l" % exp, shell=True).strip())
limit = int(subprocess.check_output("cat %s/limit" % exp, shell=True).strip())
#TODO: change this
workers = 1
gpu = 1
bits = 32 if system == "cntk" else -1
#TODO: change this
if system == "cntk":
	batch = int(subprocess.check_output("grep 'minibatchSize' %s/config.cntk | head -n 1 |  cut  -d '=' -f 2 | tr -d ' ' | tr -d '\\n'" % exp, shell=True))
else:
	batch = int(subprocess.check_output("cat %s/batch" % exp, shell=True).strip())

#re.search("(?P<system>\w+)-(?P<data>\w+)-(\w+)-h(?P<hosts>\d+)-b(?P<batch>\d+)(-w(?P<worker>\d+)-g(?P<gpu>\d+))?-l(?<limit>\d+)-(?<try>\d+)",resname)

settingv = [expname, tr, system, data, hosts, batch, workers, gpu, bits, limit]
#-------
trainv = [float(subprocess.check_output("cat %s/%s | grep %s | cut -d ':' -f 2" % (res, "timeline-stat.txt", t), shell=True).strip()) for t in train]
#-------
glob = settingv + trainv

row = glob

for host in allhosts:
	info = ''.join(subprocess.check_output("ssh -q srg@%s \"cat %s/%s/%s\"" % (host, RESS, resname, s), shell=True) for s in ("local-gpu-stats.txt","local-dstat-stats.txt"))
	#print info
	locav = [float(re.search("%s:(?P<data>\S+)" % l, info).group('data')) for l in loca]
	#print locav
	row = row + locav

print ','.join(map(str,row))




