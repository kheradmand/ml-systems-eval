import matplotlib as mpl
mpl.use('pdf')
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.backends.backend_pdf
import sys

alldata=pd.read_csv("../csv/result.csv")
cols =list(alldata.columns.values)[10:]

def timecost(filename, data, x, z, logx=True):
    pdf = matplotlib.backends.backend_pdf.PdfPages(filename)
    fig, ax = plt.subplots()
    lab =[]
    for i,group in data.sort(x).groupby(z):
        ax = group.plot(ax=ax, x=x, y="timecost_mean_mean", logx=logx, title="timecost_mean_mean", legend=False)
    	plt.close()
        lab.append(i)
    ax.legend(["%s=%d" % (z,i) for i in lab])
    pdf.savefig(fig)
    pdf.close()


def plotstats(filename, data, x, z, logx=True):
    pdf = matplotlib.backends.backend_pdf.PdfPages(filename)
    stats=8
    for metric in range(2,len(cols),stats):
	print "%d/%d" % (metric, len(cols))
	sys.stdout.flush()
        fig, axx = plt.subplots(1, stats, figsize=(4*stats,2))
    
        for stat in range(0,stats):
            ax = axx[stat]
            lab =[]
            for i,group in data.sort(x).groupby(z):
                ax = group.plot(ax=ax, x=x, y=cols[metric+stat], logx=logx, title=cols[metric+stat], legend=False)
    		plt.close()
                lab.append(i)
            #ax.legend(["#hosts=%d" % i for i in lab])   
        pdf.savefig(fig)
    pdf.close()
    plt.close()
        

for system in alldata.system.unique():
	for data in alldata.data.unique():
		subdata = alldata[(alldata.system == system) & (alldata.data == data)]
		for x in ("batch","hosts"):
			z = "hosts" if x == "batch" else "batch"
			print "system: %s data: %s x: %s" % (system, data, x)
			timecost("result/timecost-%s-%s-%s.pdf" % (system, data, x), subdata, x, z, True if x == "batch" else False)
			plotstats("result/%s-%s-%s.pdf" % (system, data, x), subdata, x, z, True if x == "batch" else False)


#mxnetmnist = alildata[(alldata.system == "mxnet") & (alldata.data == "mnist")]
#plotstats("mxnet-mnist-batch.pdf", mxnetmnist, "batch", "hosts")
