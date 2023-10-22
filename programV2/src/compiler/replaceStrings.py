from src.compiler.errors import error



def removeStringsPerLine(line, lineIndex, stringDictionary, stringCounter) -> str:
    indexList = []
    line = line.replace("\\\"", "&QUOTE")
    [indexList.append(i) for i, letter in enumerate(line) if letter == '"']
    if len(indexList) % 2 != 0:
        error(4, [lineIndex])
    if not indexList:
        return line, stringCounter
    for i in range(len(indexList)//2):
        string = line[indexList[0]:indexList[1]+1][1:-1]
        identifier = "str"+str(stringCounter)
        stringDictionary[identifier] = string
        line = line[:indexList[0]] + " "+identifier + " " +line[indexList[1]+1:]
        indexList = []
        [indexList.append(i) for i, letter in enumerate(line) if letter == '"']
        stringCounter += 1
    return line, stringCounter


def removeAllStrings(lines):
    stringDictionary = {}
    stringCounter = 0
    for lineIndex, line in enumerate(lines):
        lines[lineIndex], stringCounter = removeStringsPerLine(line, lineIndex, stringDictionary, stringCounter)
    return lines, stringDictionary

