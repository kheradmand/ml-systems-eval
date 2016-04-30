import subprocess
data =  ("mnist", "cifar10")
host = (8, 6, 4, 2)
#host = (7, 5, 3, 1)
batch = (1024, 256, 64, 16, 4)

for d in data:
        for h in host:
                for b in batch:
                        td= "lenet" if d == "cifar10" else "mlp"
                        limit= 1800 if d == "cifar10" else 600
                        name="mxnet-%s-%s-h%d-b%d-l%d" % (d, td,  h, b, limit)
                        print name
                        subprocess.call("./generate_experiment.sh %s %s %d %d %d" % (name, d, b, h, limit) , shell=True)
