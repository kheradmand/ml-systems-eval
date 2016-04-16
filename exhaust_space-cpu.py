import subprocess
data =  (10000,)
host = (1, 2, 3, 4, 5, 6, 7)
batch = (1, 8, 64, 512, 4096)  
worker=1
gpu=-1
command=1
bits=32

for d in data:
	for h in host:
		for b in batch:
			name="z_c%dd%db%dh%dw%dt%d" % (command, d, b, h, worker, bits)
			print name
			subprocess.call("cd /home/srg/eval/ && ./generate_experiment.sh %s %d %d %d %d %d %d %d" % (name, d, b, h, worker, gpu, command, bits) , shell=True)

