import pylab
import random

def flipPlot(minExp, maxExp):
    
    ratios = []
    diffs = []
    xAxis = []
    
    for exp in range(minExp , maxExp+1):
        
        xAxis.append(2**exp)
        
    for numFlips in xAxis:
        
        numHeads = 0
        for n in range(numFlips):
            
            if random.random() < 0.5:
                
                numHeads += 1
                
        numTails = numFlips - numHeads
        ratios.append(numHeads/float(numTails))
        diffs.append(abs(numHeads - numTails))
            
  #  print "ratios:"
  #  for i in range(len(ratios)):
  #      print ratios[i]
  #  
  #  print "diffs:"
  #  for i in range(len(diffs)):
  #      print diffs[i]
    print "ratios:",str(len(ratios))   
    print "diffs:",str(len(diffs))  
    print "xAxis:",str(len(xAxis))       
            
    pylab.title("Difference between Heads and Tails")
    pylab.xlabel("number of flips")
    pylab.ylabel("#heads - #tails")
    pylab.plot(xAxis,diffs,'bo')
    pylab.semilogx()
    pylab.semilogy()
    pylab.figure()
    
    pylab.title("Heads-Tails ratios")
    pylab.xlabel("number of flips")
    pylab.ylabel("heads/tails")
    pylab.plot(xAxis,ratios,'bo')
    pylab.semilogx()

    #pylab.figure()
    
   
random.seed(0)
flipPlot(4,20)
pylab.show()