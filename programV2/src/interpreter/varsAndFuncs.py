from src.interpreter.errors import error
from src.interpreter.importLibs import pyLibs
from src.interpreter.globalSGT import funcNameRIP, RIP
import src.interpreter.globalSGT
import src.interpreter.globalSGT as globalSGT

import string
from os import curdir, path
import inspect
import importlib
import json
import sys


bracesInfoVarsAndFuncs = [2]
ifChainsVarsAndFuncs = []


# Loads the function lookup table into RAM
def loadFLT() -> dict:
    try: 
        with open(path.expanduser("~")+"/.nobash/functionTable.json", "r") as f: # Reads the file in a folder in the users home directory
            return json.load(f)
    except Exception:
        errors.error(23, [])


flt = loadFLT()
vars = {"main":{}}

# Given the name of a function, get what library it is from
def getFuncLibraryName(funcName):
    try:
        libName = flt[funcName.value]["file"].replace(".py", "")
    except Exception as e:
        error(24, [funcName])
    return libName



def getFuncLibrary(funcName):
    libName = getFuncLibraryName(funcName)
    if libName in pyLibs.keys():
        return pyLibs[libName]
    error(25, [libName])




def varsAndFuncsNameCheck(name):
    cond = not any(lett for lett in name if lett not in string.ascii_letters+"_"+string.digits+":") 
    return cond



def isPyFunction(functionName: str) -> bool:
    if functionName.value in flt.keys():
        try:
            if flt[functionName.value]["language"] == "python":
                return True
            return False
        except Exception as e:
            error(20, [functionName])
    else:
        error(26, [functionName])




def isVarOrFunc(name):
    return "variable"


def getNbFuncLine(functionName):
    return flt[functionName.value]["line"]


def setVar(varName, varVal, scope=None):
    if not scope:
        scope = funcNameRIP[-1]
    if scope not in vars.keys():
        vars[scope] = {}
    vars[scope][varName] = varVal


def getBaseFunctionName(functionName): # Remove the instance of the function from the end of the function
    functionName = functionName[::-1]
    newName = ""
    for letter in functionName:
        if letter not in "1234567890":
            newName += letter
    return newName[::-1]


def passNbParameters(arguments, funcName):
    reqArgs = []
    scope = funcName
    funcName = getBaseFunctionName(funcName)
    if "arguments" in flt[funcName].keys():
        reqArgs = flt[funcName]["arguments"]
        if len(reqArgs) != len(arguments):
            error(17, [funcName, len(reqArgs), len(arguments)])
        for indx, arg in enumerate(arguments):
            setVar(reqArgs[indx], arg, scope)
    else:
        error(17, [funcName, len(arguments), 0])
            

def getBraceIdFromEndInstruction(instructionNumber):
    for brace in src.interpreter.globalSGT.bracesInfoGlobal:
        if str(brace[3].value) == str(instructionNumber):
            return brace[0]
    error(27, [ID])


def getBraceIdFromStartInstruction(instructionNumber):
    for brace in src.interpreter.globalSGT.bracesInfoGlobal:
        if str(brace[1].value) == str(instructionNumber):
            return brace[0]
    error(27, [ID])

def setObrsVars(bracesInfo):
    for braces in bracesInfo:
        ID = str(braces[0].value)
        setVar(f"cbrs{ID}", str(braces[1].value))
        setVar(f"obrs{ID}", str(braces[3].value))


def getIfChainRan(bracketID):
    for entry in globalSGT.ifChains:
        if str(bracketID.value) not in [str(id) for id in entry]:
            continue
        break
    for ifChainID in entry:
        if bracketID.value <= ifChainID.value:
            break
        if getVar("$ifResult"+str(ifChainID.value)):
            return True
    return False
    

def setRetVars(varVal):
    if varVal == None:
        return
    varName = "ret"+str(RIP[-1])
    setVar(varName, varVal, funcNameRIP[-1])


def getVar(varName):
    value, exists = hasVar(varName)
    if exists:
        return value
    error(28, [varName])


def hasVar(varName):
    scope = funcNameRIP[-1]
    if type(varName) != str:
        varName = varName.value
    if varName in vars["main"]:
        return vars["main"][varName], True
    if scope in vars.keys():
        if varName in vars[scope]:
            return vars[scope][varName], True
    return None, False

def replaceVars(arguments, funcName):
    newArgs = []
    scope = funcNameRIP[-1]
    start = -1
    noReplaceList = ["__doFor__", "__setAddVariable__",  "__setSubVariable__", "__setMulVariable__", "__setDivVariable__"]
    if funcName.value in noReplaceList :
        start = 1
    elif funcName.value == "__setVariable__":
        start = len(arguments) - 1
    for indx, arg in enumerate(arguments):
        if arg.type == "variable" and indx >= start:
            arg = getVar(arg)
        newArgs.append(arg)
    return newArgs


def isNbFunction(functionName):
    if functionName.value in flt.keys():
        try:
            if flt[functionName.value]["language"] == "nobash":
                return True
            return False
        except Exception as e:
            error(20, [functionName])
    else:
        error(26, functionName)


def addPyFuncs(libName):
    module = pyLibs[libName]
    for name, obj in inspect.getmembers(module):
        if inspect.isfunction(obj) and inspect.getmodule(obj) == module:
            flt[name] = {"language":"python", "file":libName}

    


def addNbFunctions(functions):
    for func in functions:
        if len(func) < 2:
            error(29, [func])
        flt[func[0].value] = {"language":"nobash", "line":func[1]}
        if len(func) > 2:
            flt[func[0].value]["arguments"] = [ parameter.value for parameter in func[2:]]

