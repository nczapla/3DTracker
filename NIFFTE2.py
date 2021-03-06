# This program will run through first 101 lines of data
# ensure user is in directory containing both file.txt and empty.txt
# also, task performance preform:
# data = open('NIFFTE.txt')
# import 'python filename' (likely NIFFTE2)
# 'python filename'.nif(data)
# should work out
def nif(a):
	import ast
	eventcount = 0
	e = []
	for i in range(0,101):
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
	return e




>>> data = open('NIFFTE.txt')
>>> import NIFFTE2
>>> NIFFTE2.nif(data)
[['Event', 0], [1, 30, 38, 22, 9], [1, 30, 38, 23, 10], [1, 30, 38, 24, 11], [1, 30, 39, 21, 35], [1, 30, 39, 22, 40], [1, 30, 39, 23, 44], [1, 30, 40, 20, 31], [1, 30, 40, 21, 30], [1, 30, 40, 22, 31], [1, 30, 41, 21, 18], [1, 31, 37, 26, 7], [1, 31, 37, 27, 7], [1, 31, 37, 28, 8], [1, 31, 38, 22, 10], [1, 31, 38, 23, 11], [1, 31, 38, 24, 12], [1, 31, 38, 25, 11], [1, 31, 38, 26, 9], [1, 31, 38, 27, 8], [1, 31, 38, 28, 6], [1, 31, 39, 22, 32], [1, 31, 39, 23, 33], [1, 31, 39, 24, 31], [1, 31, 39, 25, 24], [1, 31, 40, 21, 15], [1, 31, 40, 22, 13], [1, 31, 40, 23, 14], [1, 32, 35, 31, 8], [1, 32, 35, 32, 7], [1, 32, 35, 33, 7], [1, 32, 36, 28, 8], [1, 32, 36, 29, 7], [1, 32, 36, 30, 9], [1, 32, 37, 26, 23], [1, 32, 37, 27, 28], [1, 32, 37, 28, 32], [1, 32, 37, 29, 31], [1, 32, 38, 24, 22], [1, 32, 38, 25, 26], [1, 32, 38, 26, 27], [1, 32, 38, 27, 24], [1, 32, 38, 28, 18], [1, 32, 39, 24, 7], [1, 32, 39, 25, 8], [1, 32, 39, 26, 10], [1, 32, 39, 49, 1], [1, 33, 34, 33, 6], [1, 33, 34, 34, 6], [1, 33, 34, 35, 5], [1, 33, 34, 36, 5], [1, 33, 34, 37, 4], [1, 33, 34, 38, 4], [1, 33, 35, 30, 11], [1, 33, 35, 31, 14], [1, 33, 35, 32, 16], [1, 33, 35, 33, 18], [1, 33, 35, 34, 16], [1, 33, 35, 35, 13], [1, 33, 35, 36, 10], [1, 33, 36, 28, 13], [1, 33, 36, 29, 17], [1, 33, 36, 30, 20], [1, 33, 36, 31, 21], [1, 33, 36, 32, 19], [1, 33, 36, 33, 18], [1, 33, 37, 26, 5], [1, 33, 37, 27, 5], [1, 33, 37, 28, 5], [1, 33, 37, 29, 6], [1, 33, 37, 30, 6], [1, 33, 37, 31, 6], [1, 34, 33, 36, 10], [1, 34, 33, 37, 13], [1, 34, 33, 38, 17], [1, 34, 33, 39, 19], [1, 34, 33, 40, 17], [1, 34, 34, 35, 27], [1, 34, 34, 36, 26], [1, 34, 34, 37, 28], [1, 34, 36, 31, 7], [1, 34, 36, 32, 7], [1, 34, 36, 33, 7], [1, 35, 31, 41, 15], [1, 35, 31, 42, 18], [1, 35, 31, 43, 19], [1, 35, 31, 44, 18], [1, 35, 32, 37, 7], [1, 35, 32, 38, 9], [1, 35, 32, 39, 11], [1, 35, 32, 40, 14], [1, 35, 32, 41, 14], [1, 35, 32, 42, 13], [1, 35, 32, 43, 11], [1, 35, 33, 37, 7], [1, 35, 33, 38, 6], [1, 35, 33, 39, 6], [1, 35, 33, 40, 7], [1, 36, 30, 45, 35], ['Event', 1], [0, 22, 34, 48, 17]]