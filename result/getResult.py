import os

f = '.'
fs = os.listdir(f)
out = ''
for f1 in fs:
	tmp_id = f1[:3]
	if 'stat' in f1:
		g = open(f1,'r').read().split('\n')
		n = len(g)
		flag = 0
		CPI = ''
		MissRate = ''
		for i in range(0,n):
			if ('Full Run Summary' in g[i]):
				flag = 1
				line = g[i + 1].split(' ')
				for j in range(0,len(line)):
					if ('CPI:' in line[j]):
						CPI = line[j + 1]
			if ('Per Thread Demand Reference Statistics' in g[i]) and (flag > 0):
				line = g[i + 1].split(' ')
				for j in range(0,len(line)):
					if ('Rate:' in line[j]):
						MissRate = line[j + 1]
		out+= tmp_id + ' ' + f1[-1]+' ' + CPI+' ' + MissRate +'\n'
open("resultNew.out",'w').write(out)
