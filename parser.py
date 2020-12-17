# how to use the functions:
# after getting the input from discord bot,
# call parseInput with map of pickers and receivers
    # it returns a tuple

# after getting the result from the grouper,
# call parseOutput with map of pickers, receivers and output
    # it returns a map with type <String, String>

def parseOneInput(pickers):
    sortedPick = sorted(pickers)
    parseMap = {}
    for i in range(len(sortedPick)):
        parseMap[sortedPick[i]] = i
    
    parsedPickers = []
    for i in range(len(sortedPick)):
        indiList = pickers[sortedPick[i]]
        newList = []
        for j in range(len(indiList)):
            associatedNumber = parseMap[indiList[j]]
            newList.append(associatedNumber)
        parsedPickers.append()

    return parsedPickers


def parseInput(picker, receiver):
    return [parseOneInput(picker), parseOneInput(receiver)]



def parseOutput(picker, receiver, outputMap):
    sortedPick = sorted(picker)
    parseMap = {}

    sortedReceive = sorted(receiver)
    parseMap1 = {}
    for i in range(len(sortedPick)):
        parseMap[i] = sortedPick[i]
        parseMap1[i] = sortedReceive[i]
    
    parsedOutputMap = {}
    for i in outputMap:
        parsedOutputMap[parseMap[i]] = parseMap1[outputMap[i]]
    
    return parsedOutputMap
