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
	aa = list(tt) 
	lent = len(tt)-1
	bb = []
	for ii in range(40): 
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
					if aa[ii+jj][1]==0:
						jj=jj+1
					else:
						jj=jj
				ii=ii+1
	return bb