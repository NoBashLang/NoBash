from src.compiler.errors import error


def trimLines(lines):
    return [line.strip() for line in lines]

def checkForErrors(lines):
    counter = 0
    firstOpen = -1
    for index, line in enumerate(lines):
        index += 1
        if "{" in line:
            if line.count("{") != 1:
                error(5, [index])
            if line.index("{") != len(line)-1:
                error(6, [index])
            counter += 1
            if counter == 1:
                firstOpen = index
        if "}" in line:
            if line.count("}") != 1:
                error(7, [index])
            if line.index("}") != 0:
                error(8, [index])
            counter -= 1
            if counter < 0:
                error(9, [index])
    if counter > 0:
        error(10, [firstOpen])


def getControlFlowStatment(line, lineIndex):
    statements = ["while", "for", "if", "elif", "else", "func"]
    index = 0
    if line.startswith("}"): 
        index = 1
    ctrlFlowStatement = line.split()[index] 
    if ctrlFlowStatement not in statements:
        error(11, [lineIndex, ctrlFlowStatement])
    return ctrlFlowStatement


def insertId(line, braceType, id):
    return line.replace(braceType, braceType+str(id)+" ")

def createBracesInfo(bracesInfo, uniqueID):
    if str(uniqueID) not in bracesInfo.keys():
        bracesInfo[str(uniqueID)] = {}
    return bracesInfo

def indexBraces(lines):
    bracesInfo = {}
    activeList = []
    maxIdentifier = 0
    for index, line in enumerate(lines):
        if line.startswith("}"):
            try:
                uniqueID = activeList.pop()
            except Exception:
                error(9, [index])
            line = insertId(line, "}", uniqueID)
            lines[index] = line
            bracesInfo = createBracesInfo(bracesInfo, uniqueID)
            bracesInfo[str(uniqueID)]["endOp"] = index
        if line.endswith("{"):
            ctrlFlowStatement = getControlFlowStatment(line, index+1)
            lines[index] = insertId(line, "{", maxIdentifier)
            activeList.append(maxIdentifier)
            bracesInfo = createBracesInfo(bracesInfo, maxIdentifier)
            bracesInfo[str(maxIdentifier)]["startOp"] = index
            bracesInfo[str(maxIdentifier)]["ctrlFlowStatement"] = ctrlFlowStatement
            maxIdentifier += 1
    return lines, bracesInfo



def indexCurlyBraces(lines):
    lines = trimLines(lines)
    checkForErrors(lines)
    lines, bracesInfo = indexBraces(lines)
    return lines, bracesInfo

