import subprocess
host = (7, 5, 3, 1)
batch = (1000, 100, 10) 
epochs = 100

for h in host:
	for b in batch:
		name="b%dh%de%d" % (b, h, epochs)
		print name
		subprocess.call("cd /home/srg/eval/mxnet && ./generate_experiment.sh %s %d %d %d" % (name, b, h, epochs) , shell=True)

