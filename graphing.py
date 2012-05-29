# this graphs the first n lines of the NIFFTE.txt file
# also graphs a line with it
n=300
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

data=open('NIFFTE.txt')
g=nif(data)

k=0
x=[]
y=[]
z=[]
while k<n:
	if len(g[k])<3:
		k=k+1
	else:
		if g[k][0]==1:
			x.append(g[k][1])
			y.append(g[k][2])
			z.append(g[k][3])
			k=k+1
		else:
			x.append(g[k][1])
			y.append(g[k][2])
			z.append(g[k][3])
			k=k+1

import numpy as np
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
mpl.rcParams['legend.fontsize']=10

theta=np.linspace(-4*np.pi,4*np.pi,100)
z1=np.linspace(-2,2,100)
r=z1**2+1
x1=r*np.sin(theta)+20
y1=r*np.cos(theta)+30

fig=plt.figure()
ax=fig.gca(projection='3d')
ax.scatter(x,y,z,'^',c='r')
ax.plot(x1,y1,z1,label='hopefully')
ax.legend()
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
plt.show()