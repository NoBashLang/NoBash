import string

oop = ["*/", "+-", ":", ["=="], ["!="], ">", "<", ["<="], [">="], ["not"], ["and"], ["or"],"=", ["+="], ["-="], ["*="], ["/="], ["elif"], ["if"], ["else"], ["while"], ["for"], ["return"]]
noLeftOps = ["if", "elif", "for", "return", "else", "while", "for", "not"]
opFuncs = {">": "__greater__", "<": "__lesser__", "<=": "__lesserOrEqual__", ">=": "__greaterOrEqual__", "not": "__makeNot__", "=": "__setVariable__", \
    "!=": "__isNotEqual__", "for": "__doFor__", "while": "__doWhile__",  "else": "__doElse__", "return": "__funcReturn__", "for": "__doFor__", "+": "add", "-": "sub", \
    "*": "mul", "/": "div", "==":"__isEqual__", "elif": "__checkIfElse__", "if":"__checkIf__", "+=": "__setAddVariable__", "-=": "__setSubVariable__", "*=": "__setMulVariable__", \
    "/=": "__setDivVariable__", ":": "zip", "and": "__bothAnd__", "or": "__bothOr__"}


def insert(line, index, char):
    return line[:index] + char + line[index:]


def removeSpaces(line):
    toBeRejoined = ["=  =", "! =", "el if", "+  =", "-  =", "/  =", "*  ="]
    for item in toBeRejoined:
        line = line.replace(item, item.replace(" ", ""))
    return line


def insertSpaces(line):
    line = line.replace("(not ", "( not ")
    for op in ["+", ",", "-", "*", "/", "=", " if ", " in ", ")", " not "]:
        line = line.replace(op, f" {op} ")
    line = removeSpaces(line).replace(" in ", ",")
    return line


def findRightWhiteSpace(i, line, skipAmount=0):
    hitChar = False
    skippedAmount = 0
    bracketCounter = 0
    fullLine = line
    line = line[i:]
    for newI, char in enumerate(line):
        if char in string.ascii_letters + string.digits + "_":
            hitChar = True
        elif char in "()":
            if char == "(":
                bracketCounter += 1
            elif char == ")":
                bracketCounter -= 1
        elif char == " ":
            if skippedAmount != skipAmount and hitChar:
                skippedAmount += 1
                hitChar = False
                continue
            if bracketCounter == 0 and hitChar:
                new = insert(fullLine, i+newI, " ) ")
                return new

def findLeftWhiteSpace(i, line, funcToBeInserted, op):
    hitChar = False
    bracketCounter = 0
    fullLine = line
    line = line[:i]
    line = line[::-1]
    if funcToBeInserted == "__setVariable__":
        return insert(fullLine, 0, funcToBeInserted+"( ")
    elif funcToBeInserted == "__import__":
        return insert(fullLine, 0, funcToBeInserted+"( ")
    for newI, char in enumerate(line):
        if char in string.ascii_letters + string.digits + "_":
            hitChar = True
        elif char in "()":
            if char == "(":
                bracketCounter += 1
            elif char == ")":
                bracketCounter -= 1
        elif char == " ":
            if bracketCounter == 0 and hitChar:
                new = insert(fullLine, (len(line)-newI), " "+funcToBeInserted+"( ")
                return new
    if op in noLeftOps:
        return insert(fullLine, i, " "+funcToBeInserted+"( ")


def removeOp(i, line, op):
    replacer = "," if op not in noLeftOps else ""
    return line[:i] + replacer + line[i+len(op):]


def getFirstOp(line, ops):
    lowestIndex = -1
    lowestOp = ""
    for op in ops:
        if " "+op+" " in line:
            index = line.index(" "+op+" ")+1
            if lowestIndex < 0 or index < lowestIndex:
                lowestIndex = index
                lowestOp = op
    return lowestIndex, lowestOp


def doMain(line):
    line = insertSpaces(line)
    for ops in oop:
        firstOpIndex, firstOp = getFirstOp(line, ops)
        if firstOp:
            i = firstOpIndex
            line = removeOp(i, line, firstOp)
            skipAmount = 0 if firstOp != "for" else 1
            if firstOp in ["if", "elif", "else", "while", "for", "return", "import"]:
                line += ")"
                if firstOp != "else":
                    if ",{" not in line:
                        line = line.replace("{", ",{")
            else:
                line = findRightWhiteSpace(i, line, skipAmount=skipAmount)
            line = line.replace("(", "( ")
            line = findLeftWhiteSpace(i, line, opFuncs[firstOp.strip()], firstOp)
            line = doMain(line)
            return line.replace(" ", "")
    return line


def replaceOperands(lines):
    newLines = {}
    for i, line in lines.items():
        line = " " +line[0] + " "
        line = doMain(line)
        line = insertSpaces(line).replace(",", ", ")
        newLines[i] = [line]
    return newLines

