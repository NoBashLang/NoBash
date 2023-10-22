import string

from src.compiler.errors import error


def getFunctionName(line, lineNumber):
    name = ""
    for char in line[5:]:
        if char in string.ascii_letters + " ":
            name += char
        elif char == "(":
            break
        else:
            error(14, [lineNumber])
    return name.strip()

def checkBracketValidity(line, lineNumber):
    if line.count(")") == line.count("(") == 1:
        return 
    error(15, [lineNumber])


def getArgs(line):
    line = line[line.index("(")+1:line.index(")")]
    return [param.strip() for param in line.split(",")]


def getFunctionDefinitions(funcs):
    newFuncs = {}
    funcInfos = {}
    for index, func in enumerate(funcs):
        for lineNumber, line in func.items():
            line = line[0]
            funcName = getFunctionName(line, lineNumber)
            args = getArgs(line)
            del func[lineNumber]
            newFuncs[funcName] = func
            funcInfos[funcName] = args
            break
    return newFuncs, funcInfos