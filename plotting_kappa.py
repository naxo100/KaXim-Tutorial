
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import glob
import os


def read_output(filename,xlabel = "Time"):
	df = pd.read_csv(filename,sep="\t",index_col=0,comment=None)
	df.axes[0].name = xlabel
	return df

def plot_file(filename,ylbl = "Population"):
	df = read_output(filename)
	return df.plot(title = filename, ylabel = ylbl)

def plot_files(filenames = [],filter = "*",xlabel="Time",ylabel="Population",share_xy = [False,False], subplot_name = None):
	filenames = filenames + glob.glob(filter)
	filenames.sort()
	size = len(filenames)
	size_h = int(np.ceil(np.sqrt(size)))
	size_w = int(np.ceil(size/size_h))
	if(size == 2):
		size_h = 2
		size_w = 1
	
	hs = 0.15
	ws = 0.4
	if(share_xy[0] != False):
		if(subplot_name == None):
			hs = 0
		else:
			hs = 0.3
	if(share_xy[1] != False):
		ws = 0
	fig = plt.figure()
	gs = fig.add_gridspec(size_w, size_h, hspace=hs, wspace=ws)
	axs = gs.subplots(sharex = share_xy[0],sharey = share_xy[1])
	fig.supxlabel(xlabel)
	fig.supylabel(ylabel)
	#frames = list()
	i = 0
	for filename in filenames:
		if(subplot_name == ""):
			sub_title = os.path.basename(filename)
		elif(subplot_name == None):
			sub_title = None
		else:
			sub_title = subplot_name + " " + str(i)
		df = read_output(filename)
		df.plot(title = sub_title, ylabel = None,xlabel = "", ax = axs[i//size_h,i%size_h],legend = i == size_h-1)
		i = i+1
	
	return fig,axs
		


		





