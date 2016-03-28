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
	mx=(-1.0, -1, -1);
	#cpu, recv, send
    	for row in reader:
		i=i+1
		if i < 8:
			continue
		#print(row)
		mx=(max(mx[0], float(row[0])), max(mx[1], int(float(row[8]))), max(mx[2], int(float(row[9]))))
		#print mx
	print "cpup:\t%f\nrecv:\t%d\nsend:\t%d" % (mx[0], mx[1], mx[2])
