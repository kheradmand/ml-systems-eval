import csv
import sys
import os
import re
from subprocess import check_output

if len(sys.argv) != 2:
        print 'usage: time resname'
        exit()
res=sys.argv[1]
respath="/home/srg/eval/res/" + res + "/"
if not os.path.exists(respath):
        print 'result ' + res + ' does not exist'
        exit()

out=check_output("tail -n 5 " + respath + "result.txt | grep -e \"system .*elapsed\" -o | cut -d ' ' -f 2 | cut -d 'e' -f 1", shell=True)
out=out.strip()
#print out

def hh_mm_ss2seconds(hh_mm_ss):
	return reduce(lambda acc, x: acc*60 + x, map(int, map(float, hh_mm_ss.split(':'))))

print "time:\t%d" % (hh_mm_ss2seconds(out))
