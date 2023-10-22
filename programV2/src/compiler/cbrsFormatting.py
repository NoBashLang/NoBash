




def replaceCurlyBraces(lines):
    for lineNumber, line in lines.items():
        for index, segment in enumerate(line):
            lines[lineNumber][index] = segment.replace("{", "obrs").replace("}", "cbrs")
    return lines

def addToIfChains(ifChains, endOp):
    for chain in ifChains:
        chainIndexes = chain[1]
        chainIds = chain[0]


def getIfChains(bracesInfo):
    ifChains = []
    ends = {}
    conditionals = ["if", "else", "elif"]
    for braceID, info in bracesInfo.items():
        ctrlFlowStatement = info["ctrlFlowStatement"]
        if ctrlFlowStatement not in conditionals:
            continue
        startOp, endOp = info["startOp"], info["endOp"]
        ends[str(endOp)] = braceID
        if str(startOp) in ends:
            endCtrlId = ends[str(startOp)]
            for indx, chain in enumerate(ifChains):
                if endCtrlId in chain:
                    chain.append(braceID)
                    break
        else:
            ifChains.append([braceID])
    return ifChains


def getBracketWithIds(section, type):
    section = section[section.index(type)+4:]
    id = ""
    for char in section:
        if char in "1234567890":
            id += char
        else:
            return id



def getBracketInstruction(lines, funcs):
    instructions = [lines]
    instructions += [func for func in funcs.values()]
    brackets = {}
    instructionCounter = 0
    lastLine, lastLineFirstInstruction = 0, 0
    for lines in instructions:
        for lineNumber, line in lines.items():
            for section in line:
                if lineNumber != lastLine:
                    lastLineFirstInstruction = instructionCounter
                lastLine = lineNumber
                for bracketType in ["obrs", "cbrs"]:
                    if bracketType in section and not ("cbrf" in section and "obrs" in section):
                        obrsId = bracketType + getBracketWithIds(section, bracketType)
                        brackets[obrsId] = instructionCounter
                        if bracketType == "obrs":
                            brackets[obrsId] = lastLineFirstInstruction
                instructionCounter += 1
    return brackets
