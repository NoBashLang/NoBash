from src.interpreter.errors import error
from src.interpreter.varsAndFuncs import  isPyFunction, getFuncLibrary, \
    getNbFuncLine, getFuncLibraryName, addNbFunctions,isNbFunction, \
    addPyFuncs, replaceVars, setRetVars, passNbParameters, getBaseFunctionName, flt, \
    setObrsVars
import src.interpreter.globalSGT as globalSGT
from src.interpreter.importLibs import importPyLib
from src.interpreter.globalSGT import RIP, funcNameRIP
from src.interpreter.token import Token

import sys
from importlib import import_module, util
from inspect import signature
import pathlib




def lastRIP() -> int:
    if len(RIP) >= 1:
        return RIP[-1]
    error(51)


def getInstruction(instructions) -> list:
    if instructions:
        lastRip = lastRIP()
        if lastRip < len(instructions):
            return instructions[lastRip]
        error(1021, [len(instructions), lastRIP])
    error(52)


def replaceBuiltins(funcName):
    builtins = {"import": "__import__", "input": "__input__", "exit": "__exit__",\
        "list": "__list__", "dict": "___dict__", "len": "__len__", "set": "__set__",\
        "sleep": "__sleep__", "int": "__int__", "float": "__float__", "string": "__string__",\
        "bool": "__bool__", "range": "__range__", "sort": "__sort__", "split": "__split__",\
        "keys": "__keys__", "values": "__values__"}
    if funcName.value in builtins.keys():
        return Token(builtins[funcName.value])
    return funcName


def getDetails(instruction: list) -> (int, int, str, list):
    if len(instruction) < 3:
        error(63, [instruction[0], len(instruction)])
    details = [instruction[0], instruction[1], instruction[2]]
    details[2] = replaceBuiltins(details[2])
    if len(instruction) == 3:
        parameters = []
    else:
        parameters = instruction[3:]
    details.append( parameters)
    return details


def callNbFunction(functionName: str, parameters: list):
    line = getNbFuncLine(functionName)
    RIP.append(line.value+1)
    addToScope(functionName)
    if parameters:
        passNbParameters(parameters, funcNameRIP[-1])
    else:
        functionName = functionName.value
        if "arguments" in flt[functionName].keys():
            reqArgs = flt[functionName]["arguments"]
            if len(reqArgs) != 0:
                error(142, [functionName, len(parameters), len(reqArgs)])


def callPyFunction(functionName: str, parameters: list):
    lib = getFuncLibrary(functionName)
    try:
        func = getattr(lib, functionName.value)
    except Exception as e:
        error(73, [functionName.value, getFuncLibraryName(functionName)])
    retVals = None
    try:
        if not parameters:
            retVals = func()
        else:
            retVals = func(*parameters)
        return retVals
    except Exception as e:
        if len(parameters) != len(signature(func).parameters):
            error(81, [func.__name__, len(parameters), len(signature(func).parameters)])
        error(8000, e)

def advanceRIP(prevRIP, instructionsLen, RIP):
    if prevRIP == RIP:
            RIP[-1] += 1
    if RIP[-1] >= instructionsLen:
        error(1010, RIP[-1])


def extractSections(sections):
    if "Instructions" not in sections.keys():
        sys.exit(0)
    functions, bracesInfo, ifChains = [], [], []
    if "Functions" in sections.keys():
        functions = sections["Functions"]
    if "BracesInfo" in sections.keys():
        bracesInfo = sections["BracesInfo"]
    if "IfChains" in sections.keys():
        ifChains = sections["IfChains"]
    return sections["Instructions"], functions, bracesInfo, ifChains


def importMainLibs():
    importPyLib("stdlib", "~/.nobash/pylibraries/")
    addPyFuncs("stdlib")
    importPyLib("corefuncs", str(pathlib.Path(__file__).parent.resolve()))
    addPyFuncs("corefuncs")


def newScopeName(funcName):
    counter = 0
    for oldFuncName in funcNameRIP:
        if oldFuncName.startswith(funcName.value):
            counter += 1
    return funcName.value+str(counter)


def addToScope(funcName):
    funcNameRIP.append(newScopeName(funcName))


def runInstructions(sections: dict):
    importMainLibs()
    instructions, functions, bracesInfo, ifChains = extractSections(sections)
    globalSGT.init()
    globalSGT.bracesInfoGlobal = bracesInfo
    globalSGT.ifChains = ifChains
    addNbFunctions(functions)
    setObrsVars(bracesInfo)
    while True:
        prevRIP = RIP.copy()
        instruction = getInstruction(instructions)
        instNbr, lineNbr, funcName, parameters = getDetails(instruction)
        parameters = replaceVars(parameters, funcName)
        if isPyFunction(funcName):
            retVals = callPyFunction(funcName, parameters)
            setRetVars(retVals)
        elif isNbFunction:
            callNbFunction(funcName, parameters)
        else:
            error(1031, [funcName, "language"])
        advanceRIP(prevRIP, len(instructions), RIP)
        
        


