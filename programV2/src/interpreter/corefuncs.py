import sys
from src.interpreter.globalSGT import RIP, funcNameRIP
from src.interpreter.errors import error
from src.interpreter.varsAndFuncs import setVar, getVar, hasVar, \
    getBraceIdFromEndInstruction, getBraceIdFromStartInstruction, \
        getIfChainRan, addPyFuncs
from src.interpreter.token import Token
from data.pylibraries.stdlib import add, mul, div, sub
import src.interpreter.globalSGT as globalSGT
from src.interpreter.importLibs import importPyLib


def __exit__(*exitCode):
    if exitCode:
        print("Exit: ", end="")
        sys.exit(exitCode[0])
    sys.exit()


def __setVariable__(*varsAndValues):
    if len(varsAndValues) <= 1:
        error(249, [varsAndValues, RIP[-1]])
    varNames, varValue = varsAndValues[:-1], varsAndValues[-1]
    if len(varNames) == 1:
        setVar(varNames[0].value, varValue)
        return
    elif varValue.type != "list":
        error(345, [len(varNames), 1, RIP[-1]])
    elif len(varValue.value) != len(varNames):
        error(345, [len(varNames), len(varValue.value), RIP[-1]])
    for i, value in enumerate(varValue.value):
        setVar(varNames[i].value, value)


def __noopReturn__(*value):
    if len(value) == 1:
        return value[0]
    else:
        return Token(list(value), "list")


def __funcReturn__(*values):
    if len(values) == 1:
        try: 
            setVar("ret"+str(RIP[-2]), values[0], scope=funcNameRIP[-2])
        except Exception as e:
            error(1041, RIP[-1])
    elif len(values) >= 2:
        try: 
            setVar("ret"+str(RIP[-2]), Token(values, "list"), scope=funcNameRIP[-2])
        except Exception as e:
            error(1041, RIP[-1])
    RIP.pop()
    RIP[-1] = RIP[-1]+1
    if len(funcNameRIP) > 1:
        funcNameRIP.pop()
    else:
        error(10051)


def __isEqual__(x, y):
    return Token(str(x.value == y.value and x.type == y.type).lower(), "bool")


def __doWhile__(condition, endInstruction):
    try: 
        endInstruction = int(endInstruction)
    except:
        error(1045, [endInstruction])
    braceID = getBraceIdFromEndInstruction(endInstruction)
    if condition.type == "bool":
        if condition.value == "true":
            setVar(f"$whileResult{str(braceID)}", Token("true"))
            return
    RIP[-1] = endInstruction
    setVar(f"$whileResult{str(braceID)}", Token("false"))


def __jumpBackWhile__(startInstruction):
    try: 
        startInstruction = int(startInstruction)
    except:
        error(1045, [startInstruction])
    braceID = getBraceIdFromStartInstruction(startInstruction)
    if getVar(f"$whileResult{str(braceID)}"):
        RIP[-1] = startInstruction
        return


def __setAddVariable__(x, y):
    result = add(getVar(x), y)
    setVar(x.value, result)


def __setMulVariable__(x, y):
    result = mul(getVar(x), y)
    setVar(x.value, result)


def __setSubVariable__(x, y):
    result = sub(getVar(x), y)
    setVar(x.value, result)


def __setDivVariable__(x, y):
    result = div(getVar(x), y)
    setVar(x.value, result)


def __checkIf__(condition, endInstruction):
    try: 
        endInstruction = int(endInstruction)
    except:
        error(1045, [endInstruction])
    braceID = getBraceIdFromEndInstruction(endInstruction)
    setVar(f"$ifResult{str(braceID)}", Token("true"))
    if condition.type == "bool":
        if condition.value == "true":
            return
    setVar(f"$ifResult{str(braceID)}", Token("false"))
    RIP[-1] = endInstruction


def __cbrfElif__(cbrs):
    return


def __cbrfElse__(cbrs):
    return


def __checkIfElse__(condition, endInstruction):
    try: 
        endInstruction = int(endInstruction)
    except:
        error(1045, [endInstruction])
    braceID = getBraceIdFromEndInstruction(endInstruction)
    ranBefore = getIfChainRan(braceID)
    if condition.type == "bool" and not ranBefore:
        if condition.value == "true":
            setVar(f"$ifResult{str(braceID)}", Token("true"))
            return
    setVar(f"$ifResult{str(braceID)}", Token("false"))
    RIP[-1] = endInstruction


def __doElse__(endInstruction):
    try: 
        endInstruction = int(endInstruction)
    except:
        error(1045, [endInstruction])
    braceID = getBraceIdFromEndInstruction(endInstruction)
    ranBefore = getIfChainRan(braceID)
    if not ranBefore:
        setVar(f"$ifResult{str(braceID)}", Token("true"))
        return
    setVar(f"$ifResult{str(braceID)}", Token("false"))
    RIP[-1] = endInstruction


def __lesser__(x, y):
    nums = ["int", "float"]
    if x.type in nums and y.type in nums:
        return Token(str(x.value < y.value).lower(), "bool")
    elif x.type == y.type == "string":
        return Token(str(len(x.value) < len(y.value)).lower(), "bool")
    else:
        error(530, [x.type, y.type])



def __doFor__(var, dataStruct, endInstruction):
    def setVariableFor(var, dataStruct, currentIter):
        if currentIter.value >= len(dataStruct.value):
            return Token("true", "bool")
        setVar(var.value, get(dataStruct, currentIter))
        setVar(f"$forCurrentIter{str(braceID)}", Token(currentIter.value + 1))
        return Token("false", "bool")

    try: 
        endInstruction = int(endInstruction)
    except:
        error(1045, [endInstruction])
    braceID = getBraceIdFromEndInstruction(endInstruction)
    doneRunning, ranBefore = hasVar(f"$forDone{str(braceID)}")
    if not ranBefore or doneRunning:
        setVar(f"$forCurrentIter{str(braceID)}", Token(0))
    currentIter = getVar(f"$forCurrentIter{str(braceID)}")
    done = setVariableFor(var, dataStruct, currentIter)
    setVar(f"$forDone{str(braceID)}", done)
    if done:
        RIP[-1] = endInstruction
    

def ___dict__(*items): # Extra _ is needed because of shadowing
    if any([item for item in items if item.type != "zip"]):
        error(439, [item])
    dictionary = {item.value[0]: item.value[1] for item in items}
    return Token(dictionary, "dict")



def zip(x, y):
    return Token([x, y], "zip")


def __jumpBackFor__(startInstruction):
    try: 
        startInstruction = int(startInstruction)
    except:
        error(1045, [startInstruction])
    braceID = getBraceIdFromStartInstruction(startInstruction)
    if not getVar(f"$forDone{str(braceID)}"):
        RIP[-1] = startInstruction
        return


def __list__(*listItems):
    return Token(list(listItems), "list")


def __isNotEqual__(x, y):
    return Token(str(x.value != y.value or x.type != y.type).lower(), "bool")



def __cbrfIf__(cbrs):
    return


def __import__(file): # This only works for python
    if file.type == "string":
        importPyLib(file.value, "~/.nobash/pylibraries/")
        addPyFuncs(file.value)
        return
    error(435, [file, RIP[-1]])


def __bothAnd__(boolOne, boolTwo):
    if isinstance(boolOne, Token) and boolOne.type == "bool" and isinstance(boolTwo, Token) and boolTwo.type == "bool":
        result = bool(boolOne) and bool(boolTwo)
        return Token("true" if result else "false", "bool")
    else:
        error(453, [boolOne.type, boolTwo.type])

def __bothOr__(boolOne, boolTwo):
    if isinstance(boolOne, Token) and boolOne.type == "bool" and isinstance(boolTwo, Token) and boolTwo.type == "bool":
        result = bool(boolOne) or bool(boolTwo)
        return Token("true" if result else "false", "bool")
    else:
        error(454, [boolOne.type, boolTwo.type])

def __makeNot__(boolValue):
    if isinstance(boolValue, Token) and boolValue.type == "bool":
        result = not boolValue
        return Token("true" if result else "false", "bool")
    else:
        error(453, boolValue.type)
