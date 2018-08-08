import pylab

# You may have to change this path
WORDLIST_FILENAME = 'C:/Users/noura/Desktop/MOOCs/words.txt'

def loadWords():
    """
    Returns a list of valid words. Words are strings of uppercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
        #print line
    
    print "  ", len(wordList), "words loaded."
    
    return wordList

def plotVowelProportionHistogram(wordList, numBins=15):
    """
    Plots a histogram of the proportion of vowels in each word in wordList
    using the specified number of bins in numBins
    """
    
    props = []
    
    for word in wordList:
        vowels = 0.0
        pv = 0.0
        for letter in word:
            if letter in ['a', 'e', 'i', 'o', 'u'] :
                vowels += 1 
        pv = vowels/len(word)  
        #print pv
        props.append(pv)
    
   # for i in range(10):
   #      print props[i]
         
   # for i in range(100,120):
   #      print props[i]
         
    pylab.hist(props,bins=numBins)
    pylab.show()    

if __name__ == '__main__':
    wordList = loadWords()
    plotVowelProportionHistogram(wordList)
