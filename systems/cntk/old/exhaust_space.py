import subprocess
data =  (1000000,)
host = (1, 2, 3, 4, 5, 6, 7)
batch = (8, 64, 512, 4096, 32768, 262144) 
worker=1
gpu=0
command=1
bits=32

for d in data:
	for h in host:
		for b in batch:
			name="c%dd%db%dh%dw%dt%d" % (command, d, b, h, worker, bits)
			print name
			subprocess.call("cd /home/srg/eval/ && ./generate_experiment.sh %s %d %d %d %d %d %d %d" % (name, d, b, h, worker, gpu, command, bits) , shell=True)

