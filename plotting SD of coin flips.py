import pylab
import random

def runTrials(numFlips):
    
    numHeads = 0
    for n in range(numFlips):
            
            if random.random() < 0.5:
                
                numHeads += 1
                
    numTails = numFlips - numHeads
    return numHeads, numTails

def sdv(L):

    mean = sum(L)/float(len(L))
    tot = 0
    for i in L:
        tot += (i-mean)**2
    
    return (tot / len(L))**0.5

      
def flipPlot(minExp, maxExp, numTrials):
    
    meanRatios, meanDiffs, sdRatios, sdDiffs = [],[],[],[]
    xAxis = []
    
    for exp in range(minExp , maxExp+1):        
        xAxis.append(2**exp)
        
    for numFlips in xAxis:
        
        ratios, diffs = [],[]
        for t in range(numTrials):
            numHeads, numTails = runTrials(numFlips)
            ratios.append(numHeads/float(numTails))
            diffs.append(abs(numHeads - numTails))
        
        meanRatios.append(sum(ratios)/numTrials)
        meanDiffs.append(sum(diffs)/numTrials)
        sdRatios.append(sdv(ratios))
        sdDiffs.append(sdv(diffs))    
                    
  #  print "ratios:"
  #  for i in range(len(ratios)):
  #      print ratios[i]
  #  
  #  print "diffs:"
  #  for i in range(len(diffs)):
  #      print diffs[i]
  #  print "diffs:",str(len(diffs))  
  #  print "xAxis:",str(len(xAxis))       
            
    pylab.title("Ratios Mean")
    pylab.xlabel("number of flips")
    pylab.ylabel("Mean of Head to Tail ratio")
    pylab.plot(xAxis,meanRatios,'bo')
    pylab.semilogx()
    pylab.figure()
    
    pylab.title("Ratios Standard Deviation")
    pylab.xlabel("number of flips")
    pylab.ylabel("SDV of Head to Tail ratio")
    pylab.plot(xAxis,sdRatios,'bo')
    pylab.semilogx()
    pylab.semilogy()
    pylab.figure()
    
    pylab.title("Differences Mean")
    pylab.xlabel("number of flips")
    pylab.ylabel("Mean of difference between Heads and Tails")
    pylab.plot(xAxis,meanDiffs,'bo')
    pylab.semilogx()
    pylab.semilogy()
    pylab.figure()
    
    pylab.title("Differences Standard Deviation")
    pylab.xlabel("number of flips")
    pylab.ylabel("SDV of difference between Heads and Tails")
    pylab.plot(xAxis,sdDiffs,'bo')
    pylab.semilogx()
    pylab.semilogy()
 
    
    #pylab.figure()
    
   
random.seed(0)
flipPlot(4,20,20)
pylab.show()