import csv
import sys
import os
import re
if len(sys.argv) != 2:
        print 'usage: gpeak resname'
        exit()
res=sys.argv[1]
respath="/home/srg/eval/res/" + res + "/"
if not os.path.exists(respath):
        print 'result ' + res + ' does not exist'
        exit()

with open(respath + 'gstat.txt', 'r') as f:
	gpumax=-1
	memmax=-1
	for line in f:
		match=re.search("\|\s+(?P<gpu>\d+)\%\s+Default\s+\|", line)
		if not match is None:
			#print match.group('gpu')	
			gpu = int(match.group('gpu'))
			gpumax = max(gpumax, gpu)
		
		match=re.search("C\s+cntk\s+(?P<mem>\d+)\D+\s+\|", line)
                if not match is None:
			#print match.group('mem')
                        mem = int(match.group('mem'))
                        memmax = max(memmax, mem)	
	print "gpu:\t%d\nmem:\t%d" % (gpumax, memmax)
