import string
import re

from src.compiler.errors import error

def insertFunctionCall(line, index):
    return line[:index] + "__noopReturn__" + line[index:]

def getOutermostBrackets(line): # MUST BE REDONE FOR ARGS W MUTLIPLE FUNCS
    if "(" not in line or ")" not in line:
        return -1, -1
    brCounter = 0
    for closeIndex, char in enumerate(line):
        if char == "(":
            brCounter += 1
        elif char == ")":
            brCounter -= 1
            if brCounter == 0:
                break
    return line.index("("), closeIndex


def detectFunctionCall(line, index):
    fullLine = line
    line = line[:index]
    line = line[::-1]
    foundFunctionChars = False
    lastFunctionChars = 0
    for char in line:
        if char in string.ascii_letters + "_":
            lastFunctionChars += 1
        else:
            break
    if not lastFunctionChars > 0:
        fullLine = insertFunctionCall("".join(fullLine), index)
        lastFunctionChars = len("__noopReturn__")
    return index - lastFunctionChars, fullLine


def getArguments(firstBracket, secondBracket, line):
    args = []
    currentArg = ""
    bracketCounter = 0
    line = line[firstBracket+1:secondBracket]
    for char in line:
        if char == "," and bracketCounter == 0:
            args.append(currentArg)
            currentArg = ""
            continue
        if char == "(":
            bracketCounter += 1
        elif char == ")":
            bracketCounter -= 1
        elif char == " ":
            continue
        currentArg += char
    args.append(currentArg)
    return args


def checkBracketValidity(line, lineIndex):
    bracketCounter = 0
    for index, char in enumerate(line):
        if char == "(":
            bracketCounter += 1
        elif char == ")":
            bracketCounter -= 1
            if bracketCounter < 0:
                error(12, [lineIndex])
    if bracketCounter != 0:
        error(13, [lineIndex])


def splitFunctionCalls(lineList, firstCall=True):
    changed = False
    newLineList = lineList
    for lineIndex, line in enumerate(lineList):
        checkBracketValidity(line, newLineList)
        firstBracketLine, secondBracketLine = getOutermostBrackets(line)
        if firstBracketLine == secondBracketLine == -1:
            continue
        startIndex, line = detectFunctionCall(line, firstBracketLine)
        args = getArguments(firstBracketLine, secondBracketLine, line)
        for index, arg in enumerate(args):
            firstBracket, secondBracket = getOutermostBrackets(arg)
            if firstBracket == secondBracket == -1:
                continue
            changed = True
            startIndex, arg = detectFunctionCall(arg, firstBracket)
            newLineList.append(arg)
            args[index] = "ret"+str(len(newLineList))+" "
        newLineList[lineIndex] = line[:firstBracketLine+1] + ", ".join(args) + line[secondBracketLine:]
    lineList = newLineList
    if changed:
        lineList = splitFunctionCalls(lineList, firstCall=False)    
    if firstCall:
        lineList = lineList[::-1]
        lineList = setCbrfIfLast(lineList)
    return lineList


def decrementRetNumbers(match):
    number = int(match.group(1))
    incremented_number = number - 1
    return f"ret{incremented_number}"


def decrementReturnValues(lineList):
    pattern = r'ret(\d+)'
    for i, line in enumerate(lineList):
        line = re.sub(pattern, decrementRetNumbers, line)
        lineList[i] = line
    return lineList


def setCbrfIfLast(lineList):
    if lineList[-1].startswith("__cbrf"):
        lineList = [lineList[-1]] + lineList[:-1]
        lineList = decrementReturnValues(lineList)
    return lineList


def getFullRet(segment, index):
    segment = segment[index:]
    for i, char in enumerate(segment):
        if char not in string.ascii_letters + "1234567890":
            return index + i


def insertProperRetVals(line, retCounter):
    for indx, segment in enumerate(line):
        newSegment = ""
        while "ret" in segment:
            startIndex, endIndex = segment.index("ret"), getFullRet(segment, segment.index("ret"))
            ret = segment[startIndex:endIndex]
            if len(ret) <= 3:
                break
            if segment[segment.index("ret")+3] not in "1234567890":
                segment = segment[endIndex:]
                continue
            retNum = len(line) - int(ret[3:]) + retCounter
            newSegment += segment[:startIndex] + " ret"+str(retNum)
            segment = segment[endIndex:]     
        line[indx] = newSegment + segment
    return line, len(line) + retCounter



def runSplit(lineDict, retCounter):
    newDict = {}
    for index, lineList in lineDict.items():
        # lineList = [line.replace(",", " , ") for line in lineList]
        lineList = splitFunctionCalls(lineList)
        newDict[index], retCounter = insertProperRetVals(lineList, retCounter)
    return newDict, retCounter


def splitFuncCalls(lines, funcs):
    functionStartInstructions = {}
    retCounter = 0
    lines, retCounter = runSplit(lines, retCounter)
    for functionName, functionLines in funcs.items():
        functionStartInstructions[functionName] = retCounter
        funcs[functionName], retCounter = runSplit(functionLines, retCounter)
    return lines, funcs, functionStartInstructions


