import sys
from os import path, listdir
import importlib
from src.interpreter.token import Token
from src.interpreter.globalSGT import RIP
from src.interpreter.errors import error





def get(dataStruct, index):
    if dataStruct.type == "list":
        if index.type != "int":
            error(303, [index.type])
        return dataStruct.value[index.value]


def add(x, y):
    nums = ["int", "float"]
    if x.type in nums and y.type in nums:
        return Token(x.value + y.value, "float")
    elif x.type == y.type == "string":
        return Token(x.value + y.value, "string")
    error(305, [x.type, y.type])
    

def mul(x, y):
    nums = ["int", "float"]
    if x.type in nums and y.type in nums:
        return Token(x.value * y.value, "float")
    elif x.type == "string" and y.type == "int":
        return Token(x.value * y.value, "string")
    elif x.type == "int" and y.type == "string":
        return Token(x.value * y.value, "string")
    error(306, [x.type, y.type])


def div(x, y):
    nums = ["int", "float"]
    if x.type in nums and y.type in nums:
        if int(y.value) == 0:
            error(343, [y.value, RIP[-1]])
        return Token(x.value / y.value, "float")
    error(306, [x.type, y.type, RIP[-1]])


def neg(x):
    if x.type in ["int", "float"]:
        x.value = -x.value
        return x
    error(304, [x.type, RIP[-1]]) 


def sub(x, y):
    nums = ["int", "float"]
    if x.type in nums and y.type in nums:
        return Token(x.value - y.value)

def put(*msg):
    print(*msg)


def __float__(value):
    if value.type == "int":
        return Token(float(value.value), "float")
    elif value.type == "string":
        try:
            return Token(float(value.value), "float")
        except Exception:
            pass    
    error(307, [value.type, value.value, RIP[-1]])


def __int__(value):
    if value.type == "float":
        return Token(int(value.value), "int")
    elif value.type == "string":
        try:
            return Token(int(value.value), "float")
        except Exception:
            pass    
    error(308, [value.type, value.value, RIP[-1]])


def fmt(formatString, *values):
    if formatString.type != "string":
        error(309, [formatString.type, formatString.value, RIP[-1]])
    for value in values:
        formatString.value = formatString.value.replace("%v", str(value))
    return formatString 





def string(value):
    if value.type in ["int", "float", "string"]:
        return Token(str(value.value), "string")
    error(309, [value.type, value.value, RIP[-1]])


def __bool__(value):
    if value.type in ["int", "float", "string"]:
        return Token(bool(value.value), "bool")  
    error(310, [value.type, value.value, RIP[-1]])


def putnl(*msg):
    print(*msg, end="")


def __input__():
    return Token(input(), "string")


def __len__(value):
    if value.type not in ["string", "list", "dictionary"]:
        error(311, [value.type, value.value, RIP[-1]])
    return Token(len(value.value), "int")


def sort(start):
    if start.type in ["list", "string"]:
        return Token(sorted(start.value), start.type)
    error(313, [start.type, start.value, RIP[-1]])
    


def reverse(start):
    if start.type in ["list", "string"]:
        return Token(start.value[::-1], start.type)
    error(314, [start.type, start.value, RIP[-1]])


def trim(value, start, end):
    if value.type not in ["list", "string"]:
        error(315, [value.type, value.value, RIP[-1]])
    if start.type != "int":
        error(316, [start.type, start.value, RIP[-1]])
    elif start.value < 0 or start.value > len(value.value) or start.value > end.value:
        error(319, [start.value, end.value, len(value.value), RIP[-1]])
    if end.type != "int": 
        error(317, [end.type, end.value, RIP[-1]])
    elif end.value < 0 or end.value > len(value.value):
        error(318, [end.value, len(value.value), RIP[-1]])
    result = Token(value.value[start.value:end.value], value.type)
    return result
    

def range(start, end):
    if start.type != "int":
        error(320, [start.type, start.value, RIP[-1]])
    elif end.type != "int":
        error(321, [end.type, end.value, RIP[-1]])
    numberList = list(range(start.value, end.value))
    return Token(numberList, "list")


def split(inputString, identifier):
    if inputString.type != "string":
        error(324, [inputString.type, RIP[-1]])
    elif identifier.type != "string":
        error(324, [identifier.type, RIP[-1]])
    return Token(split(inputString.value, identifier.value), "list")


def append(listToken, item):
    if isinstance(listToken, Token) and listToken.type == "list":
        listValue = listToken.value
        listValue.append(item)
        return Token(listValue, "list")
    else:
        error(8100, "The first argument must be of type Token with a list value")


def replace(original, pattern, newValue):
    if original.type == "string":
        if pattern.type != "string":
            error(327, [pattern.type, RIP[-1]])
        if newValue.type != "string":
            error(326, [newValue.type, RIP[-1]])
        return Token(original.value.replace(pattern.value, newValue.value), "string")
    error(323, [original.type, RIP[-1]])


def writef(fileName, contents):
    if fileName.type != "string":
        error(322, [fileName.type, RIP[-1]])
    elif contents.type != "string":
        error(323, [contents.type, RIP[-1]])
    try: 
        with open(fileName.value, "w") as file:
            file.write(contents.value)
    except Exception as e:
        error(324, [fileName.value, str(e)])


def appendf(fileName, contents):
    if fileName.type != "string":
        error(322, [fileName.type, RIP[-1]])
    elif contents.type != "string":
        error(323, [contents.type, RIP[-1]])
    try: 
        with open(fileName.value, "a") as file:
            file.write(contents.value)
    except Exception as e:
        error(325, [fileName.value, str(e)])


# Read
def readf(fileName):
    if fileName.type != "string":
        error(322, [fileName.type, RIP[-1]])
    try:
        with open(fileName.value, "r") as file:
            contents = file.read()
            return Token(str(contents), "string")
    except Exception as e:
        error(325, [fileName.value, str(e)])


def has(container, item):
    def isSame(x, y):
        return Token(str(x.value == y.value and x.type == y.type).lower(), "bool")

    if container.type in ["list", "dict"]:
        return Token(str(any([isSame(element, item) for element in container.value])).lower(), "bool")
    elif container.type == "string":
        if item.type != "string":
            error(345, [item.type, RIP[-1]])
        return Token(str(item.value in container.value).lower(), "string")
    error(346, [container.type, RIP[-1]])


def get(container, identifier):
    def isSame(x, y):
        return Token(str(x.value == y.value and x.type == y.type).lower(), "bool")

    if container.type == "list":
        if identifier.type != "int":
            error(358, [identifier.type])
        elif identifier.value < 0 or identifier.value >= len(container.value):
            error(359, [identifier.value, len(container.value)])
        for containerIdentifier, value in enumerate(container.value):
            if containerIdentifier == identifier.value:
                return value
        error(357, [container.type, identifier.value])
    elif container.type == "dict":
        if not has(container, identifier):
            error(357, [container.type, identifier.value])
        for containerIdentifier, value in container.value.items():
            if isSame(containerIdentifier, identifier):
                return value 
    
    error(356, [container.type])


# List/dict set
def __set__(container, identifier, newValue):
    def isSame(x, y):
        return Token(str(x.value == y.value and x.type == y.type).lower(), "bool")

    if container.type == "list":
        if identifier.type != "int":
            error(358, [identifier.type])
        elif identifier.value < 0 or identifier.value >= len(container.value):
            error(359, [identifier.value, len(container.value)])
        newContainer = container.value.copy()
        newContainer[identifier.value] = newValue
        return Token(newContainer, "list")
    elif container.type == "dict":
        if not has(container, identifier):
            error(357, [container.type, identifier.value])
        for containerIdentifier, value in container.value.items():
            if isSame(containerIdentifier, identifier):
                newContainer = container.value.copy()
                newContainer[containerIdentifier] = newValue
                return Token(newContainer, "dict")
    
    error(356, [container.type])

# Keys
def keys(dictionary):
    if isinstance(dictionary, Token) and dictionary.type == "dict":
        return Token(list(dictionary.keys()), "list")
    else:
        error(357, [dictionary.type])

# Values
def keys(dictionary):
    if isinstance(dictionary, Token) and dictionary.type == "dict":
        return Token(list(dictionary.values()), "list")
    else:
        error(357, [dictionary.type])


def __string__(value):
    return Token(str(value.value), "string")


def __int__(value):
    try:
        return Token(int(value.value), "number")
    except ValueError:
        error(690, [value.type])


def __float__(value):
    try:
        return Token(float(value.value), "number")
    except ValueError:
        error(691, [value.type])


def __bool__(value):
    if value.value.lower() == "true" or value.value.lower() == "false":
        return Token(value.value, "bool")
    else:
        error(690, [value.type])
