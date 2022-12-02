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

#stretch goal map the edps curve for each 

units = ["", "k", "m", "b", "t"]
#we could just make a function that uses it as a string and adds 3 0's each iteration but nah. I have to add the units manually anyway
unitMultiplexer = [1, 1000, 1000000, 1000000000, 1000000000000]

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
    return tofloat * unitMultiplexer[unitIndex]

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
        ["lettuce", 3, "13.1m", 7.5],
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

    prettyPrint(results)

def alignItem(data, width, padding):
    returnString = ""
    rightPadding = ""
    i = 0
    while (i < (width-len(data))): # there will be a way to push to a string x number of times without a while loop
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