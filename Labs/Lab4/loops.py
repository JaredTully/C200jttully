def evenCount(aList):
    evenList = []
    if type(aList) != list:
        return -1
    else:
        for x in aList:
            if (x % 2 == 0):
                evenList += [x]
        return len(evenList)

def getSecondHalfOfString(fullStr):
    return (fullStr[(len(fullStr) / 2):])

def getFirstHalfOfString(fullStr):
    return (fullStr[0: (len(fullStr) / 2) ])

def manualStringToList(newStr):
    returnList = []

    for x in range(0, len(newStr)):
        returnList += newStr[x]

    return returnList

def sumOfOddNumbers(numList):
    total = 0
    for x in numList:
        if (x % 2) != 0:
            total += x
    return total
