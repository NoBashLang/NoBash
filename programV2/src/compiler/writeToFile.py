from src.compiler.errors import error
from os.path import expanduser, basename


def insertStrings(line, stringDictionary):
    for replacer, string in dict(reversed(list(stringDictionary.items()))).items():
        line = line.replace(replacer, '"'+string+'"')
    return line


def writeLine(line, file, instructionCount, lineNumber, stringDictionary):
    if "(" not in line or ")" not in line:
        line = "__noopReturn__()"
    line = line.replace("(", ", ").replace(")", "").strip()
    line = line[:-1] if line.endswith(",") else line
    line += "\n"
    line = insertStrings(line, stringDictionary)
    file.write(f"{instructionCount}, {lineNumber}, "+line)


def writeFuncsToFile(funcInfos, functionStartInstructions, file):
    file.write("# Functions\n")
    for functionName, parameters in funcInfos.items():
        startInstruction = functionStartInstructions[functionName]
        toWrite = f"{functionName}, {str(startInstruction-1)}, {', '.join(parameters)}".strip()
        toWrite = toWrite[:-1] if toWrite.endswith(",") else toWrite
        file.write(toWrite+"\n")


def writeLinesToFile(lines, functions, scriptName, stringDictionary, file):
    for func in functions.values():
        for key, value in func.items():
            lines[key] = value
    instructionCount = 0
    file.write("# Instructions\n")
    for lineNumber, line in lines.items():
        for instruction in line:
            writeLine(instruction, file, instructionCount, lineNumber, stringDictionary)
            instructionCount += 1


def writeBracesInfoToFile(ifChains, bracesInfo, file, bracesInstructions):
    if ifChains:
        file.write("# IfChains\n")
        [file.write(", ".join(chain)+"\n") for chain in ifChains]
    if bracesInfo and bracesInstructions:
        file.write("# BracesInfo\n")
        for id, data in bracesInfo.items():
            try: 
                openingInstruction = str(bracesInstructions["obrs"+str(id)])
                closingInstruction = str(bracesInstructions["cbrs"+str(id)])
                file.write(f"{id}, {openingInstruction}, {data['ctrlFlowStatement']}, {closingInstruction}\n")
            except Exception as e:
                continue


def writeMetadataToFile(file, metadata):
    file.write("# Metadata\n")
    for name, data in metadata.items():
        file.write(f"{name}, {data}\n")


def writeDataToFile(lines, functions, scriptName, stringDictionary, funcInfos, functionStartInstructions, ifChains, bracesInfo, bracesInstructions, metadata):
    try:
        pathPrefix = expanduser("~/.nobash/compiledScripts/")
        scriptName = basename(scriptName)
        with open(pathPrefix+scriptName.replace(".nb", ".nbc"), "w") as file:
            writeMetadataToFile(file, metadata)
            writeLinesToFile(lines, functions, scriptName, stringDictionary, file)
            writeFuncsToFile(funcInfos, functionStartInstructions, file)
            writeBracesInfoToFile(ifChains, bracesInfo, file, bracesInstructions)
    except Exception as e:
        error(16, [scriptName.replace(".nb", ".nbc")])


