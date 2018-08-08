import pylab

L = [1,2,3,4,5,4,2,3]
#pylab.plot(L)
pylab.hist(L,bins=5)
pylab.xlim(0,10)
pylab.ylim(0,10)

pylab.show()