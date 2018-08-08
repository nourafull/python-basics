
N = 3
for i in xrange(2**N):
    combo = []
    for j in xrange(N):
        print "i",str(i)
        print "j",str(j)
        print i >> j
       # print (i >> j) % 2
        print "\n"
        
    #    if (i >> j) % 2 == 1:
    #        combo.append(items[j])
    #yield combo