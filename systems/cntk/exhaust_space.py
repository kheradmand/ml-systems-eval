import subprocess
data =  ("mnist", "cifar10")
host = (7, 5, 3, 1)
batch = (1024, 256, 64, 16, 4)
worker=1
gpu=0
bits=32

for d in data:
	for h in host:
		for b in batch:
			td= "lenet" if d == "cifar10" else "mlp"
			limit= 1800 if d == "cifar10" else 600
			name="cntk-%s-%s-h%d-b%d-w%d-g%d-t%d-l%d" % (d, td,  h, b, worker, gpu, bits, limit)
			print name
			subprocess.call("./generate_experiment.sh %s %s %d %d %d %d %d %d" % (name, d, b, h, worker, gpu, bits, limit) , shell=True)

