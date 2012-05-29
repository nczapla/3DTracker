from array import *
def beta(filename,n):
	import numpy as np
	def nif(a):
		import ast
		eventcount=0
		e=[]
		for i in range(0,n):
			b=a.readline()
			c=b.split(' ')
			d=[]
			if '####' in b:
				event=['Event',eventcount]
				e.append(event)
				eventcount=eventcount+1
			else:
				for j in range(0,5):
					t=ast.literal_eval(c[j])
					d.append(t)
				e.append(d)
		return e
	data=open(filename)
	g=nif(data)
	k=0
	Q=0
	q=0
	while q<n:
		if len(g[q])<3:
			q=q+1
		else:
			q=q+1
			Q=Q+1
	x=np.zeros(Q)
	y=np.zeros(Q)
	z=np.zeros(Q)
	XC=0
	while k<n:
		if len(g[k])<3:
			k=k+1
		else:
			if g[k][0]==1:
				x[XC]=g[k][1]
				y[XC]=g[k][2]
				z[XC]=g[k][3]
				k=k+1
				XC=XC+1
			else:
				x[XC]=g[k][1]
				y[XC]=g[k][2]
				z[XC]=g[k][3]
				k=k+1
				XC=XC+1
	import matplotlib as mpl
	import mpl_toolkits.mplot3d as m3d
	from mpl_toolkits.mplot3d import Axes3D
	import matplotlib.pyplot as plt
	data= np.concatenate((x[:,np.newaxis],y[:, np.newaxis], z[:, np.newaxis]), axis = 1)
	mean_data = data.mean(axis = 0)
	aa, bb, cc = np.linalg.svd(data - mean_data)
	#Change the arguments of np.mgrid to the average distance between particles
	line_points = cc[0] * np.mgrid[-50:50:2j][:, np.newaxis]
	line_points += mean_data
	mpl.rcParams['legend.fontsize']=20
	theta=np.linspace(-4*np.pi,4*np.pi,100)
	graph_axis = m3d.Axes3D(plt.figure())
	graph_axis.scatter3D(*data.T,c='r')
	graph_axis.plot3D(*line_points.T,label='best fit')
	graph_axis.legend()
	graph_axis.set_xlabel('X Label')
	graph_axis.set_ylabel('Y Label')
	graph_axis.set_zlabel('Z Label')
	plt.show()