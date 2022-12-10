import math
import re
#given input arrays of format:
#name, quantity, dollarsUnits, timePeriod in seconds, level
#eg
#["bread", 3, "1.3k", 1.3, 2]
#["cakes", 2, "3.1m", 32, 250]
#["milkshakes", 1, "12t", 45, 152]
#["tea", 1, "1.8m", 26, 71]
#produce an "effective $/s" metric
#and then sort it
#effective dollars per second = ($/s)*n

#stretch goal map the edps/cost curve for each food

units = ["", "k", "m", "b", "t", "aa", "ab", "ac", "ad", "ae", "af", "ag", "ah", "ai", "aj", "ak", "al"]

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
    if (unitIndex != 0): #or if targetstring.isAlpha. the same thing really but the digit comparison is probably faster
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
        ["Limestone", 4, "6.25ah", 2.2, 764],
        ["Coal", 4, "980ag", 3.8, 701],
        ["Iron", 4, "1.13ah", 5.5, 625],
        ["Copper", 4, "141ag", 7.2, 562],
        ["Sulphur", 4, "20.8ah", 8.8, 540],
        ["Sapphire", 4, "3.47ah", 13.8, 343],
        ["Gold", 4, "2.06ah", 10.5, 462],
        ["Jade", 4, "1.62ah", 12.2, 402],
        ["Ruby", 4, "1.16ah", 15.5, 269],
        ["Amethyst", 4, "4.18ah", 17.2, 222],
        ["Diamond", 3, "8.92ah", 18.8, 163],
        ["Obsidian", 3, "88.8ah", 20.5, 115],
    ]
    
    i = 0
    results = []
    while (i < len(data)):
        unitIndex = getUnit(data[i][2])
        fullDollars = normalise(data[i][2], unitIndex)
        edps = getEdps(fullDollars, data[i][1], data[i][3])
        formattedEdps = f"{int(edps):.3E}"
        formattedEdpsLevel = f"{int(edps/data[i][4]):.3E}"
        results.append([data[i][0], edps, edps/data[i][4], formattedEdps, formattedEdpsLevel])
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
    col2Width = len(max(data, key=lambda d: lenFunc(d, 3))[3].__str__()) + 3
    col3Width = len(max(data, key=lambda d: lenFunc(d, 4))[4].__str__()) + 3
    
    padding = "  "
    
    #header
    header = alignItem("Name", col1Width, padding) + "|" + alignItem("EDPS", col2Width, padding) + "|" + alignItem("EDPS/Level", col3Width, padding) + "|"
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
        tempresult += alignItem(line[3].__str__(), col2Width, padding) + "|"
        tempresult += alignItem(line[4].__str__(), col3Width, padding) + "|"

        print (tempresult)
        i += 1
    
    print(hr)
main()