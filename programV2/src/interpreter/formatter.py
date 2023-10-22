from src.interpreter.token import Token
from src.interpreter.errors import error


def findStrings(line: str) -> (int, int):
    if line.count('"') >= 2:
        first = line.index('"')
        return first, line[first+1:].index('"')+first+1

    return 0, 0



def stringRemover(stringList: dict, line: str) -> str:
    string = None
    for _ in range(line.count('"')//2):
        stringEntry = f"str{len(stringList)+1}"
        start, stop = findStrings(line)
        string = line[start:stop]+'"'
        line = line[:start]+ stringEntry + line[stop+1:]
        stringList[stringEntry] = string
    return line


def removeStrings(sections: dict, stringList: dict):
    for section, lines in sections.items():
        lines = [stringRemover(stringList, line) for line in lines]
        sections[section] = lines
    return sections


def stringAdder(line: str, stringList: dict):
    for index, item in enumerate(line):
        if item in stringList.keys():
            line[index] = stringList[item].replace("&QUOTE", '"').replace("\\n", "\n")
    return line


def addStrings(sections: dict, stringList: dict):
    for section, lines in sections.items():
        sections[section] = [stringAdder(line, stringList) for line in lines]
    return sections
    


def splitSections(rawLines: str) -> dict:
    sections = {}
    section = None
    for line in rawLines:
        if line.startswith("# ") and len(line.split()) == 2:
            section = line.split()[1]
        elif section:
            if section not in sections.keys():
                sections[section] = []
            sections[section].append(line)
    return sections


def splitUp(sections):
    for section, lines in sections.items():
        sections[section] = [[item.strip() for item in line.split(", ")] for line in lines]
    return sections


def setTokens(sections: dict):
    for section, values in sections.items():
        sections[section] = [[Token(token) for token in line] for line in values]
    return sections


def verifyInstructionNumbers(instructions) -> bool:
    for indx, instruction in enumerate(instructions):
        intIndx = 0
        try:
            intIndx = int(instruction[0].value)
        except Exception:
            error(62, instruction[0].value)
        if intIndx != indx:
            error(61, [instruction[0].value, indx])


def removeMetadata(sections):
    if "Metadata" not in sections.keys():
        return
    del sections["Metadata"]
    return sections


def format(rawLines) -> dict(): # Note: Even though dict replacements happen in-place, we still set it again for clarity
    stringList = {}
    sections = splitSections(rawLines)
    sections = removeMetadata(sections)
    sections = removeStrings(sections, stringList)
    sections = splitUp(sections)
    sections = addStrings(sections, stringList)
    sections = setTokens(sections)
    verifyInstructionNumbers(sections["Instructions"])
    return sections