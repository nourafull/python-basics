def powerset():
    ps = []
    for j in range(3):
        for k in range(3):
            for l in range(3):    
                ps.append([j,k,l])
    
    return ps
                
def two_knapsacks(items):
    N = len(items)
    L = powerset()
    combo = []
    for i in range(3**N):
        
        bag1 = []
        bag2 = []
        
        for j in range(len(items)):
            if L[i][j] == 1:
                bag1.append(items[j])
            elif L[i][j] == 2:
                bag2.append(items[j])
        
        combo.append((bag1,bag2))

    return combo
    
items = ['clock','vase','book']
powerset()
Q = two_knapsacks(items)


for i in Q:
    print i
        
