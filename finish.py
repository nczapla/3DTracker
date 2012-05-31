from array import *
import numpy as np
import matplotlib as mpl
import mpl_toolkits.mplot3d as m3d
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

def nif(a):
	import ast
	eventcount = 0
	e = []
	for i in range(0,50):
		b = a.readline()
		c = b.split(' ')
		d = []	
		if '####' in b:
			event = ['Event', eventcount]
			e.append(event)
			eventcount = eventcount + 1
		else:
			for j in range(0,5):
				t = ast.literal_eval(c[j])
				d.append(t)
			e.append(d)
			"""f = compare(e)"""
	return e


def compare(tt):
	fig=plt.figure()
	ax=fig.gca(projection='3d')
	aa = list(tt) 
	lent = len(tt)-1
	bb = []
	ii=1
	x=[]
	y=[]
	z=[]
	while ii in range(40): 
		if aa[ii][1]==0:
			ii=ii+1
		else:
			jj = 1
			if aa[ii+jj][1]==0:
				jj=jj+1
			else:
				while aa[ii+jj][4] - aa[ii][4] > 5:
					bb.append(aa[ii+jj])
					jj = jj + 1
					x.append(aa[ii+jj][1])
					"""y.append(aa[ii+jj][2])"""
					"""z.append(aa[ii+jj][3])"""
					X=array('f',x)
					"""Y=array('f',y)"""
					"""Z=array('f',z)"""
					"""ax.scatter(X,Y,Z,c='b')"""
					"""ax.scatter(x,y,z,c='r')"""
					if aa[ii+jj][1]==0:
						jj=jj+1
					else:
						jj=jj
				ii=ii+1
	"""plt.show()"""
	return bb
	