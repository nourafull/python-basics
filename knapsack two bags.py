
def powerSet(items):
    N = len(items)
    x = []
    for i in xrange(2**N):
        bag1 = []
        bag2 = []
        for j in xrange(N):
            
            if (i >> j) % 2 == 1:
                combo.append(items[j])
                
        x.append(combo)
    return x
        

L = ['book','clock','vase']
#for p in powerSet(L):
#    print p

Q = powerSet(L)
for e in Q:
    print e
