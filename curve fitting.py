import pylab, random

def getData(fileName):
    dataFile = open(fileName, 'r')
    distances = []
    masses = []
    discardHeader = dataFile.readline()
    for line in dataFile:
        d, m = line.split()
        distances.append(float(d))
        masses.append(float(m))
    dataFile.close()
    return (masses, distances)



def fitData2(fileName):
    xVals, yVals = getData(fileName)
    xVals = pylab.array(xVals)
    yVals = pylab.array(yVals)
    xVals = xVals*9.81  # convert mass to force (F = mg)
    pylab.plot(xVals, yVals, 'bo', label = 'Measured points')
    pylab.title('Measured Displacement of Spring')
    pylab.xlabel('Force (Newtons)')
    pylab.ylabel('Distance (meters)')
    a,b,c = pylab.polyfit(xVals, yVals, 2)  # fit y = ax**2 + bx + c
   
    # use line equation to graph predicted values
    
    estYVals = a*(xVals**2) + b*xVals + c
    k = 1/a
    print estYVals
    print k
    pylab.plot(xVals, estYVals, label = 'Polynomial fit, k = '
               + str(round(k, 5)))
    pylab.legend(loc = 'best')

fitData2('C:/Users/noura/Desktop/MOOCs/springData.txt')
pylab.show()