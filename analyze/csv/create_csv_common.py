import sys
import os
import subprocess
sys.path.append("../../common/")
from common import *



hosts = subprocess.check_output("cat %s | grep Mustang" % HOSTS, shell=True).strip().split('\n')

setting = ["expname","try","system","data","hosts","batch","worker","gpu","bits","limit"]
train = ["timecost_mean_mean", "iterations_min"]
gpumetrics = ["gpu", "gpumem"]
dstatmetrics = ["usr","sys","idl","wai","hiq","siq","used","buff","cach","free","recv","send","read","writ","read","writ","tot","tcp","udp","raw","frg"]
metrics = gpumetrics + dstatmetrics
#stats = ["entries", "mean", "std", "var", "median", "min", "max", "ninetieth"] 
stats =  ["mean", "median", "ninetieth", "max", "min", "std", "var", "entries"]


glob = setting + train
loca = ["%s_%s" % (metric, stat) for metric in metrics for stat in stats]
 



