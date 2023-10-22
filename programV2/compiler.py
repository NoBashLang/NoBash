from src.compiler.readInput import readFile
from src.compiler.getMetadata import getData
from src.compiler.replaceStrings import removeAllStrings
from src.compiler.curlyBracesIndexer import indexCurlyBraces
from src.compiler.linesToDict import turnLinesToDict
from src.compiler.cleanupEmpty import cleanUp
from src.compiler.operandsReplacer import replaceOperands
from src.compiler.funcCallSplitter import splitFuncCalls
from src.compiler.makeClosingBracketReturns import makeCBRF
from src.compiler.getFuncDefinitions import getFunctionDefinitions
from src.compiler.cbrsFormatting import replaceCurlyBraces, getIfChains, getBracketInstruction
from src.compiler.writeToFile import writeDataToFile
from src.compiler.errors import error

from sys import argv

# Repeats a function for both lines and functions
def forLinesAndFuncs(lines, funcs, operation, params=None):
    if params:
        lines = operation(lines, *params)
    else:
        lines = operation(lines)
    if isinstance(funcs, list):
        for index, func in enumerate(funcs):
            if params:
                funcs[index] = operation(func, *params)
            else:
                funcs[index] = operation(func)
    else:
        for funcName, func in funcs.items():
            if params:
                funcs[indfuncNameex] = operation(func, *params)
            else:
                funcs[funcName] = operation(func)
    return lines, funcs


# Calls every level one by one
if __name__ == "__main__":
    try:
        fileLocation = argv[1]
    except Exception:
        error(18)
    lines = readFile(fileLocation)
    metadata = getData(fileLocation)
    lines, stringDictionary = removeAllStrings(lines)
    lines, bracesInfo = indexCurlyBraces(lines)
    lines = turnLinesToDict(lines)
    lines, funcs = cleanUp(lines, bracesInfo)
    lines, funcs = forLinesAndFuncs(lines, funcs, replaceOperands)
    lines, funcs = forLinesAndFuncs(lines, funcs, makeCBRF, [bracesInfo])
    funcs, funcInfos = getFunctionDefinitions(funcs)
    lines, funcs, functionStartInstructions = splitFuncCalls(lines, funcs)
    lines, funcs = forLinesAndFuncs(lines, funcs, replaceCurlyBraces)
    ifChains = getIfChains(bracesInfo)
    bracesInstructions = getBracketInstruction(lines, funcs)
    writeDataToFile(lines, funcs, fileLocation, stringDictionary, funcInfos, \
        functionStartInstructions, ifChains, bracesInfo, bracesInstructions, metadata)
    exit(0)