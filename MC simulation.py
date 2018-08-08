import random

def noReplacementSimulation(numTrials):
  
    
    x = 0
    for i in range(numTrials): 
        red = 3
        green = 3
        totalBalls = 6
    
        for j in range(3):
            b = random.random()
            if b < 0.5 :
                red -= 1
            else:
                green -= 1
            totalBalls -= 1
            print "b=",str(b),"\n red=",str(red),"\n green=",str(green)
       
        if red == 0 or green == 0 :
            x += 1
        print "x = ",str(x)        
    
    probx = x/float(numTrials)
    print "probx = ",str(probx)
    return probx
    
print noReplacementSimulation(10)