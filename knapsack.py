def powerSet(L):
    """Returns all subsets of size 0 - len(some_list) for some_list"""
    if len(L) == 0:
        # If the list is empty, return the empty list
        return [[]]
    ps = []
    first = L[0]
    rest = L[1:]
    
    for e in powerSet(rest):
        
        ps.append(e)
        
        next_subset = e + [first]
        ps.append(next_subset)
        
    return ps

def get_sumWeights(e):
      totw = 0
      for z in e:
           totw += z[2]
      return totw

def get_sumValues(e):     
      sum = 0
      for z in e:
           sum += z[1]
      return sum  
        
names = ['clock', 'painting', 'radio', 'vase', 'book','computer']
vals = [175,90,20,50,10,200]
weights = [10,9,4,2,1,20]
maxw = 20

L = []
V = []
for i in range(len(names)):
    L.append((names[i],vals[i],weights[i]))
    V.append(0)
    
    
  
Q = powerSet(L)
subset = []
for e in Q:
   if len(e) == 0 :
       totw = 0  
   else:
       totw = get_sumWeights(e)   
   if totw <= maxw :
       subset.append(e)

for e in subset:
    print e
    
    
hVI = 0
hV = 0
for i in range(len(subset)):
    newValue = get_sumValues(subset[i])
    if newValue > hV :
        hV = newValue
        hVI = i

print subset[hVI]
print hV 
        
       




