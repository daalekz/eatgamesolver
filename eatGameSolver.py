import math
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

#stretch goal map the edps curve for each unitMultiplexer

units = ["", "k", "m", "b", "t", "aa", "ab", "ac", "ad", "ae", "af"]
# unitMultiplexer = [1, 3, 6, 9, 12, 13, 15, 18, 21, 23]

def getUnit(target):
    #if its a number with no unit attached (between 1-1000)
    if (target.isalpha()):
        return 0
    i = 1
    while (i < len(units)):
        if (target.endswith(units[i])):
            return i;
            break;
        else:
            i += 1

def normalise(targetString, unitIndex):
    parsedString = targetString
    if (unitIndex != 0): #or if targetstring.isAlpha. the same thing really but the digit comparison is faster 
        parsedString = parsedString[0:len(parsedString)-1]
    tofloat = float(parsedString)
    return tofloat * powIndex(unitIndex)

def powIndex(unitIndex):
    if (unitIndex == 0):
        return 1
    return pow(10, unitIndex * 3)

def getEdps(fullNumber, quantity, time):
    result = (fullNumber/time) * quantity
    return result.__floor__()

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
        ["lettuce", 1, "12k", 1.2],
        ["coconut", 3, "20.5m", 12.5],
        ["carrot", 2, "14.9m", 35],
    ]
    
    i = 0
    results = []
    while (i < len(data)):
        unitIndex = getUnit(data[i][2])
        fullDollars = normalise(data[i][2], unitIndex)
        edps = getEdps(fullDollars, data[i][1], data[i][3])
        results.append([data[i][0], edps])
        i += 1

    results.sort(reverse = True, key=sortFunc)
    prettyPrint(results)

def sortFunc(d):
    return d[1]

def alignItem(data, width, padding):
    returnString = ""
    rightPadding = ""
    i = 0
    # surely there will be a way to push to a string x number of times without a while loop
    while (i < (width-len(data))): 
        rightPadding += " "
        i += 1
    
    returnString = (padding + data + rightPadding + padding)
    return returnString

def prettyPrint(data):
    
    width = 10
    padding = "  "
    
    #header
    header = alignItem("Name", width, padding) + "|" + alignItem("EDPS", width, padding) + "|"
    i = 0

    #Horizontal rule
    hr = ""
    while (i < len(header)):
        hr += "-"
        i += 1

    print (header)
    print (hr)

    #body
    i = 0
    while (i < len(data)):
        tempresult = ""
        line = data[i]

        tempresult = alignItem(line[0], width, padding) + "|"
        tempresult += alignItem(line[1].__str__(), width, padding) + "|"
        print (tempresult)
        i += 1
    
    print(hr)

main()