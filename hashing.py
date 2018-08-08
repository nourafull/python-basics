import random


class intDict(object):
    """A dictionary with integer keys"""
    
    def __init__(self, numBuckets):
        """Create an empty dictionary"""
        self.buckets = []
        self.numBuckets = numBuckets
        for i in range(numBuckets):
            self.buckets.append([])
            
    def addEntry(self, dictKey, dictVal):
        """Assumes dictKey an int.  Adds an entry."""
        hashBucket = self.buckets[dictKey%self.numBuckets]
        #print "dictKey%self.numBuckets = ",str(dictKey%self.numBuckets)
        print hashBucket
        for i in range(len(hashBucket)):
            print hashBucket[i][0]
            if hashBucket[i][0] == dictKey:
                hashBucket[i] = (dictKey, dictVal)
                return
        hashBucket.append((dictKey, dictVal))
        print "key and value have been appended to bucket num ", str(dictKey%self.numBuckets)
        
    def getValue(self, dictKey):
        """Assumes dictKey an int.  Returns entry associated
           with the key dictKey"""
        hashBucket = self.buckets[dictKey%self.numBuckets]
        for e in hashBucket:
            if e[0] == dictKey:
                return e[1]
        return None
    
    def __str__(self):
        res = '{'
        for b in self.buckets:
            for t in b:
                res = res + str(t[0]) + ':' + str(t[1]) + ','
        return res[:-1] + '}' #res[:-1] removes the last comma


D = intDict(29)

for i in range(20):
    #choose a random int in range(10**5)
    key = random.choice(range(10**5))
    print "adding",str(key)," : ",str(i)
    D.addEntry(key, i)

print '\n', 'The buckets after insertion are:'
for hashBucket in D.buckets: #violates abstraction barrier
    print '  ', hashBucket

print '\n'















