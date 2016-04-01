import subprocess
data =  (10000,)
host = (1, 2, 3, 4, 5, 6, 7)
batch = (1, 5, 10, 50, 100, 500, 1000, 5000, 10000) 
worker=1
gpu=-1

for d in data:
	for h in host:
		for b in batch:
			name="z_d%db%dh%dw%d" % (d, b, h, worker)
			print name
			subprocess.call("cd /home/srg/eval/ && ./generate_experiment.sh %s %d %d %d %d %d" % (name, d, b, h, worker, gpu) , shell=True)

