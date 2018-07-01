import numpy as np
import matplotlib.pyplot as plt

alldata = open("result.out",'r').read().split('\n')[:-1]

alldata = sorted(alldata)

r0 = []
r1 = []
r2 = []
pgm = []

c0 = []
c1 = []
c2 = []

for line in alldata:
	lst = line.split(' ')
	if lst[1]=='0':
		pgm.append(lst[0])
		r0.append(float(lst[3]))
		c0.append(float(lst[2]))
	if lst[1]=='1':
		r1.append(float(lst[3]))
		c1.append(float(lst[2]))
	#if lst[1]=='2':
	#	r2.append(float(lst[3]))
	#	c2.append(float(lst[2]))

alldata = open("result.out",'r').read().split('\n')[:-1]
alldata = sorted(alldata)

for line in alldata:
	lst = line.split(' ')
	if lst[1]=='2':
		r2.append(float(lst[3]))
		c2.append(float(lst[2]))

n = len(pgm)
pgm = pgm[:n]
r0 = np.array(r0[:n])
r1 = np.array(r1[:n])
r2 = np.array(r2[:n])

c0 = np.array(c0[:n])
c1 = np.array(c1[:n])
c2 = np.array(c2[:n])

fig=plt.figure(1)
ax1 = plt.subplot(111)

# bar_width = 0.35
# x_bar = np.arange(len(pgm)) * 2.
# ax1.bar(x_bar - bar_width , r0, width=bar_width , color='r')
# ax1.bar(x_bar , r1, width=bar_width , color='g')
# ax1.bar(x_bar +  bar_width, r2, width=bar_width , color='b')
# ax1.set_xticks(x_bar)
# ax1.set_xticklabels(pgm)
# ax1.set_xlabel('Program Id')
# ax1.set_ylabel('MissRate(%)')
# ax1.legend(['LRU','random','FreqSample'])
# ax1.set_title('MissRate on LRU,random,FreqSample')
# plt.show()
print (r1.sum() - r2.sum())/float(r0.shape[0])
print (c1.sum() - c2.sum())/float(r0.shape[0])
bar_width = 0.35
x_bar = np.arange(len(pgm)) * 2.
ax1.bar(x_bar - bar_width , c0, width=bar_width , color='r')
ax1.bar(x_bar , c1, width=bar_width , color='g')
ax1.bar(x_bar +  bar_width, c2, width=bar_width , color='b')
ax1.set_xticks(x_bar)
ax1.set_xticklabels(pgm)
ax1.set_xlabel('Program Id')
ax1.set_ylabel('CPI')
ax1.legend(['LRU','random','FreqSample'])
ax1.set_title('CPI on LRU,random,FreqSample')
#plt.show()

