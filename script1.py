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
			d = compare(e)
	return d


def compare(tt):
	aa = list(tt) 
	lent = len(tt)-1
	bb = []
	for ii in range(50): 
		jj = 1
		while aa[ii+jj][5] - aa[ii][5] > 5:
			bb.append(aa[ii+jj])
			jj = jj + 1
			if ii + jj >= lent:
				break
		if ii + jj >= lent:
			break
		ii = ii + jj
return bb