import sys
from os import path, listdir
import importlib
from src.interpreter.token import Token
from src.interpreter.globalSGT import RIP
from src.interpreter.errors import error




def add(x, y):
    nums = ["int", "float"]
    if x.type in nums and y.type in nums:
        return Token(x.value + y.value, "float")
    elif x.type == y.type == "string":
        return Token(x.value + y.value, "string")
    error(30, [x.type, y.type])
    

def mul(x, y):
    nums = ["int", "float"]
    if x.type in nums and y.type in nums:
        return Token(x.value * y.value, "float")
    elif x.type == "string" and y.type == "int":
        return Token(x.value * y.value, "string")
    elif x.type == "int" and y.type == "string":
        return Token(x.value * y.value, "string")
    error(30, [x.type, y.type])


def div(x, y):
    nums = ["int", "float"]
    if x.type in nums and y.type in nums:
        if int(y.value) == 0:
            error(343, [y.value])
        return Token(x.value / y.value, "float")
    error(30, [x.type, y.type])


def neg(x):
    if x.type in ["int", "float"]:
        x.value = -x.value
        return x
    error(32, [x.type]) 


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
    error(33, [value.type, value.value])


def __int__(value):
    if value.type == "float":
        return Token(int(value.value), "int")
    elif value.type == "string":
        try:
            return Token(int(value.value), "float")
        except Exception:
            pass    
    error(33, [value.type, value.value])


def fmt(formatString, *values):
    if formatString.type != "string":
        error(33, [formatString.type, formatString.value])
    for value in values:
        formatString.value = formatString.value.replace("%v", str(value), 1)
    return formatString 





def string(value):
    if value.type in ["int", "float", "string"]:
        return Token(str(value.value), "string")
    error(33, [value.type, value.value])


def __bool__(value):
    if value.type in ["int", "float", "string"]:
        return Token(bool(value.value), "bool")  
    error(33, [value.type, value.value])


def putnl(*msg):
    print(*msg, end="")


def __input__():
    return Token(input(), "string")


def __len__(value):
    if value.type not in ["string", "list", "dictionary"]:
        error(33, [value.type, value.value])
    return Token(len(value.value), "int")


def __sort__(start):
    startType = start.type
    if start.type in ["list", "string"]:
        start = start.value
        if startType == "list":
            start = {token.value: token.type for token in start}
            print("s", start)
            sortedList = [Token(token, tokenType) for token, tokenType in dict(sorted(start.items())).items()]
            return Token(sortedList, startType)
        return Token(sorted(start), "string")
    error(33, [start.type, start.value])
    


def reverse(start):
    if start.type in ["list", "string"]:
        return Token(start.value[::-1], start.type)
    error(33, [start.type, start.value])


def trim(value, start, end):
    if value.type not in ["list", "string"]:
        error(33, [value.type, value.value ])
    if start.type != "int":
        error(33, [start.type, start.value ])
    elif start.value < 0 or start.value > len(value.value) or start.value > end.value:
        error(34, [start.value, end.value, len(value.value) ])
    if end.type != "int": 
        error(33, [end.type, end.value ])
    elif end.value < 0 or end.value > len(value.value):
        error(34, [start.value, end.value, len(value.value) ])
    result = Token(value.value[start.value:end.value], value.type)
    return result
    

def __range__(start, end):
    if start.type != "int":
        error(33, [start.type, start.value])
    elif end.type != "int":
        error(33, [end.type, end.value])
    numberList = list(range(start.value, end.value))
    numberList = [Token(number, "int") for number in numberList]
    return Token(numberList, "list")


def __split__(inputString, identifier):
    if inputString.type != "string":
        error(33, [inputString.type, inputString.value])
    elif identifier.type != "string":
        error(33, [identifier.type, inputString.value])
    splitList = inputString.value.split(identifier.value)
    splitList = [Token(value, "string") for value in splitList] 
    return Token(splitList, "list")


def append(listToken, item):
    if isinstance(listToken, Token) and listToken.type == "list":
        listValue = listToken.value
        listValue.append(item)
        return Token(listValue, "list")
    else:
        error(33, [listToken.value, listToken.type])


def replace(original, pattern, newValue):
    if original.type == "string":
        if pattern.type != "string":
            error(33, [pattern.type, pattern.value])
        if newValue.type != "string":
            error(33, [newValue.type, newValue.value])
        return Token(original.value.replace(pattern.value, newValue.value), "string")
    error(33, [original.type, original.value])


def writef(fileName, contents):
    if fileName.type != "string":
        error(33, [fileName.type, fileName.value])
    elif contents.type != "string":
        error(33, [contents.type, contents.value])
    try: 
        with open(fileName.value, "w") as file:
            file.write(contents.value)
    except Exception as e:
        error(35, [fileName.value, str(e)])


def appendf(fileName, contents):
    if fileName.type != "string":
        error(33, [fileName.type, fileName.value])
    elif contents.type != "string":
        error(33, [contents.type, contents.value])
    try: 
        with open(fileName.value, "a") as file:
            file.write(contents.value)
    except Exception as e:
        error(35, [fileName.value, str(e)])


# Read
def readf(fileName):
    if fileName.type != "string":
        error(33, [fileName.type, fileName.value])
    try:
        with open(fileName.value, "r") as file:
            contents = file.read()
            return Token(str(contents), "string")
    except Exception as e:
        error(35, [fileName.value, str(e)])


def has(container, item):
    def isSame(x, y):
        return Token(str(x.value == y.value and x.type == y.type).lower(), "bool")

    if container.type in ["list", "dict"]:
        return Token(str(any([isSame(element, item) for element in container.value])).lower(), "bool")
    elif container.type == "string":
        if item.type != "string":
            error(33, [item.type, item.value])
        return Token(str(item.value in container.value).lower(), "string")
    error(33, [container.type, container.value])


def get(container, identifier):
    def isSame(x, y):
        return Token(str(x.value == y.value and x.type == y.type).lower(), "bool")

    if container.type == "list":
        if identifier.type != "int":
            error(33, [identifier.type, identifier.value])
        elif identifier.value < 0 or identifier.value >= len(container.value):
            error(36, [identifier.value, len(container.value)])
        for containerIdentifier, value in enumerate(container.value):
            if containerIdentifier == identifier.value:
                return value
        error(33, [container.type, identifier.value])
    elif container.type == "dict":
        if not has(container, identifier):
            error(37, [container.type, identifier.value])
        for containerIdentifier, value in container.value.items():
            if isSame(containerIdentifier, identifier):
                return value 
    
    error(32, [container.type])


# List/dict set
def __set__(container, identifier, newValue):
    def isSame(x, y):
        return Token(str(x.value == y.value and x.type == y.type).lower(), "bool")

    if container.type == "list":
        if identifier.type != "int":
            error(32, [identifier.type])
        elif identifier.value < 0 or identifier.value >= len(container.value):
            error(36, [identifier.value, len(container.value)])
        newContainer = container.value.copy()
        newContainer[identifier.value] = newValue
        return Token(newContainer, "list")
    elif container.type == "dict":
        newContainer = container.value.copy()
        newContainer[identifier] = newValue
        return Token(newContainer, "dict")
    
    error(32, [container.type])

# Keys
def __keys__(dictionary):
    if isinstance(dictionary, Token) and dictionary.type == "dict":
        return Token(list(dictionary.value.keys()), "list")
    else:
        error(32, [dictionary.type])

# Values
def __values__(dictionary):
    if isinstance(dictionary, Token) and dictionary.type == "dict":
        return Token(list(dictionary.value.values()), "list")
    else:
        error(32, [dictionary.type])


def __string__(value):
    return Token(str(value.value), "string")
