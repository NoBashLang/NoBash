

def separateFunctions(lines, bracesInfo):
    funcs = []
    currentFunc = {}
    for info in bracesInfo.values():
        removeOps = []
        if "ctrlFlowStatement" not in info.keys():
            continue
        if info["ctrlFlowStatement"] != "func":
            continue
        startOp, endOp = int(info["startOp"]), int(info["endOp"])
        for op in range(startOp, endOp+1):
            if str(op) not in lines:
                continue
            currentFunc[str(op)] = lines[str(op)]
            removeOps.append(str(op))
        removeOps = list(set(removeOps))
        for op in removeOps:
            del lines[op]
        funcs.append(currentFunc)
        currentFunc = {}
    return lines, funcs
    



def cleanUp(lines, bracesInfo):
    emptyIndexes = []
    for index, lineList in lines.items():
        line = lineList[0]
        if "//" in line:
            line = line[:line.index("//")].strip()
        lines[index] = [line]
        if not line:
            emptyIndexes.append(index)
    for index in emptyIndexes:    
        del lines[index]
    lines, funcs = separateFunctions(lines, bracesInfo)
    return lines, funcs