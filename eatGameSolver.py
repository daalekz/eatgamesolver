import math
import re
#given input arrays of format:
#name quantity dollarsUnits timePeriod in seconds 
#eg
#["bread", 3, "1.3k", "1.3"]
#["cakes", 2, "3.1m", "32"]
#["milkshakes", 1, "12t", "45"]
#["tea", 1, "1.8m", "26"]
#produce an "effective $/s" metric
#and then sort it
#effective dollars per second = ($/s)*n

#stretch goal map the edps/cost curve for each food

units = ["", "k", "m", "b", "t", "aa", "ab", "ac", "ad", "ae", "af"]

def getUnit(target):
    #if its a number with no unit attached (between 1-1000)
    if (target.isalpha()):
        return 0
    i = len(units) - 1
    while (i > 1): #we go backwards so we can use "endswith". units should (?) keep getting longer the higher we go. if they get smaller but share latters with other entries (eg input of af when ["af", "q", "aff"]). will probably need to do a regex split then find it.
        if (target.endswith(units[i])):
            return i;
            break;
        else:
            i -= 1

def normalise(targetString, unitIndex):
    parsedString = targetString
    if (unitIndex != 0): #or if targetstring.isAlpha. the same thing really but the digit comparison is faster 
        parsedString = parsedString[0:len(parsedString)-len(units[unitIndex])]
    tofloat = float(parsedString)
    return tofloat * powIndex(unitIndex)

def powIndex(unitIndex):
    if (unitIndex == 0):
        return 1
    return pow(10, unitIndex * 3)

def getEdps(fullNumber, quantity, time):
    result = (fullNumber/time) * quantity
    return result

def tests():
    testString = "343k"
    myUnit = getUnit(testString)
    #unit test lol
    print("expecting a 0 for input: ", testString, "got: ", myUnit)

    fullNumber = normalise(testString, myUnit)
    print("fullnumber for input: ", testString, " was: ", fullNumber)

def main():
    # tests()
    data = [ #moon data
        ["lettuce", 4, "82.8aa", 3.8],
        ["coconut", 3, "121aa", 6.3],
        ["carrot", 4, "371aa", 8.8],
        ["pepper", 3, "53.6aa", 22.5],
        ["orange", 3, "576aa", 27.5],
        ["mushroom", 2, "1.05ab", 32.5],
        ["banana", 2, "33.2ab", 75]
    ]
    
    i = 0
    results = []
    while (i < len(data)):
        unitIndex = getUnit(data[i][2])
        fullDollars = normalise(data[i][2], unitIndex)
        edps = getEdps(fullDollars, data[i][1], data[i][3])
        results.append([data[i][0], edps])
        i += 1

    results.sort(reverse = True, key= lambda d: sortFunc(d, 1))
    prettyPrint(results)

def sortFunc(d, x):
    return d[x]

def lenFunc(d, x):
    return len(d[x].__str__())

def alignItem(data, width, padding):
    returnString = ""
    rightPadding = ""
    i = 0

    rightPadding = " " * (width-len(data)) #concat to string n times

    returnString = (padding + data + rightPadding + padding)
    return returnString

def prettyPrint(data):
    #clean these two colwidths up.
    #returns length of longest entry in the list + 3
    col1Width = len(max(data, key=lambda d: lenFunc(d, 0))[0].__str__()) + 3
    col2Width = len(max(data, key=lambda d: lenFunc(d, 1))[1].__str__()) + 3
    padding = "  "
    
    #header
    header = alignItem("Name", col1Width, padding) + "|" + alignItem("EDPS", col2Width, padding) + "|"
    i = 0

    #Horizontal rule
    hr = "-" * len(header)

    print (header)
    print (hr)

    #body
    i = 0
    while (i < len(data)):
        tempresult = ""
        line = data[i]

        tempresult = alignItem(line[0], col1Width, padding) + "|"
        tempresult += alignItem(line[1].__str__(), col2Width, padding) + "|"
        print (tempresult)
        i += 1
    
    print(hr)

main()