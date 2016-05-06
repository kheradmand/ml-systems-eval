import matplotlib as mpl
mpl.use('pdf')
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.backends.backend_pdf
import sys

alldata=pd.read_csv("../csv/result.csv")
cols =list(alldata.columns.values)[10:]


def plotstats(filename, data, x, z, logx=True):
    markers = ["o","h","p","s","d","*","v","^","<"]
    pdf = matplotlib.backends.backend_pdf.PdfPages(filename)
    alias = {"gpu":"gpu usage (%)", "usr":"cpu usage (%)", "recv": "network receive rate (B/sec)", "send": "network send rate (B/sec)"}
    for stat in ["mean"]:
        for metric in ["gpu","usr","recv","send"]:
            fig, axx = plt.subplots(1, 2, figsize=(8,4), sharey=True)
            for j,machine in enumerate(["M07", "M11"]):
                ax = axx[j]
                lab =[]
                counter = 0
                for i,group in data.sort(x).groupby(z):
                    counter = counter + 1
                    y="%s_%s_%s" % (machine, metric, stat)
                    group.plot(ax=ax, x=x, y=y, logx=logx, title= "server" if machine == "M07" else "client", legend=False, style="-"+markers[counter], sharey=True)
                    if machine == "M07":
                            ax.set_ylabel(alias[metric])
                    lab.append(i)
            h,l = ax.get_legend_handles_labels()
            plt.tight_layout()
            #lgd = plt.figlegend(h, ["%s=%d" % (z,i) for i in lab], loc="best", ncol = len(lab) / (1 if z == "batch" else 2))  
            lgd = plt.figlegend(h, ["%s=%d" % (z,i) for i in lab], loc='center left', bbox_to_anchor=(0.97, 0.5))  
#            fig.show()
            pdf.savefig(fig, bbox_extra_artists=(lgd,), bbox_inches='tight')
    pdf.close()
    plt.close()

for system in alldata.system.unique():
        for data in alldata.data.unique():
                subdata = alldata[(alldata.system == system) & (alldata.data == data)]
                for x in ("batch","hosts"):
                        z = "hosts" if x == "batch" else "batch"
                        print "system: %s data: %s x: %s" % (system, data, x)
                        plotstats("result/minimal-%s-%s-%s.pdf" % (system, data, x), subdata, x, z, True if x == "batch" else False)

