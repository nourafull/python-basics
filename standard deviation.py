import math


def sdl(L):
    
    
    mean = sum(L) / len(L)
   
    x = 0
    for e in L:
        x += (e - mean)**2
    x = float(x)
    sd = math.sqrt(x / len(L))
    return sd
    
L1 = [10, 4, 12, 15, 20, 5]
mean = sum(L1)/len(L1)
print mean
print sdl(L1)/mean
