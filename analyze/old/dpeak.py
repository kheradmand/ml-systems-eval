import csv
import sys
import os

if len(sys.argv) != 2:
        print 'usage: dpeak resname'
        exit()
res=sys.argv[1]
respath="/home/srg/eval/res/" + res + "/"
if not os.path.exists(respath):
        print 'result ' + res + ' does not exist'
        exit()

with open(respath + 'dstat.csv', 'rb') as f:
	reader = csv.reader(f)
	i=0
	mx=(-1.0, -1, -1, -1, -1, -1, -1, -1);
	#cpu, mem, recv, send, iord, iowt, dski, dsko 
    	for row in reader:
		i=i+1
		if i < 8:
			continue
		#print(row)
		mx=(max(mx[0], float(row[0])), max(mx[1], int(float(row[6]))), max(mx[2], int(float(row[10]))), max(mx[3], int(float(row[11]))), max(mx[4], int(float(row[12]))), max(mx[5], int(float(row[13]))), max(mx[6], int(float(row[14]))), max(mx[7], int(float(row[15]))))
		#print mx
	print "cpup:\t%f\nmemc:\t%d\nrecv:\t%d\nsend:\t%d\niord:\t%d\niowt:\t%d\ndski:\t%d\ndsko:\t%d" % mx
