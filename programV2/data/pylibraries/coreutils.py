from src.interpreter.errors import error
from src.interpreter.token import Token
from datetime import datetime
from time import sleep

import shutil
import os
import time
import platform


def ls(*args):
    directory = "."
    options = {"all": False, "files": False, "directoriesOnly": False}

    for arg in args:
        if isinstance(arg, Token) and arg.type == "string":
            directory = arg.value
        elif isinstance(arg, Token) and arg.type == "zip":
            if len(arg.value) == 2:
                keyToken, value = arg.value
                if keyToken.value in options:
                    key = keyToken.value
                    if isinstance(value, Token) and value.type == "bool":
                        options[key] = value.value
    
    directory = os.path.expanduser(directory)

    try:
        if options["all"]:
            fileList = os.listdir(directory)
        else:
            if options["directoriesOnly"]:
                fileList = [item for item in os.listdir(directory) if os.path.isdir(os.path.join(directory, item))]
            else:
                fileList = [item for item in os.listdir(directory) if not options["files"] or os.path.isfile(os.path.join(directory, item))]
                
        if not options["all"]:
            fileList = [item for item in fileList if not item.startswith(".")]
                
        fileList = [Token(item, "string") for item in fileList]

        return Token(fileList, "list")
    except Exception as e:
        error(8100, str(e))

def cd(directory):
    if isinstance(directory, Token) and directory.type == "string":
        try:
            os.chdir(os.path.expanduser(directory.value))
            return Token("true", "bool")
        except Exception as e:
            return Token("false", "bool")
    else:
        error(8100, "Directory must be of type string")
        return Token("false", "bool")


def ln(source, target):
    if isinstance(source, Token) and isinstance(target, Token) and source.type == "string" and target.type == "string":
        try:
            os.symlink(source.value, target.value)
            return Token("true", "bool")
        except Exception as e:
            return Token("false", "bool")
    else:
        error(8100, "Both source and target must be of type string")


def mkdir(directory):
    if isinstance(directory, Token) and directory.type == "string":
        try:
            os.mkdir(directory.value)
            return Token("true", "bool")
        except Exception as e:
            return Token("false", "bool")
    else:
        error(8100, "Directory must be of type string")


def mv(source, destination):
    if isinstance(source, Token) and isinstance(destination, Token) and source.type == "string" and destination.type == "string":
        try:
            shutil.move(source.value, destination.value)
            return Token("true", "bool")
        except Exception as e:
            return Token("false", "bool")
    else:
        error(8100, "Both source and destination must be of type string")


def rm(*args):
    path = None
    recursive = False

    for arg in args:
        if isinstance(arg, Token) and arg.type == "string":
            path = arg.value
        elif isinstance(arg, Token) and arg.type == "zip":
            if len(arg.value) == 2:
                keyToken, value = arg.value
                key = keyToken.value
                if key == "recursive" and isinstance(value, Token) and value.type == "bool":
                    recursive = value.value

    if path is not None:
        try:
            if os.path.isfile(path):
                os.remove(path)
            elif os.path.isdir(path):
                if recursive:
                    shutil.rmtree(path)
            return Token("true", "bool")
        except Exception as e:
            return Token("false", "bool")
    else:
        error(8100, "Path must be of type string")


def rmdir(directory):
    if isinstance(directory, Token) and directory.type == "string":
        try:
            os.rmdir(directory.value)
            return Token("true", "bool")
        except Exception as e:
            error(8100, str(e))
    else:
        error(8100, "Directory must be of type string")


def uniq(list1, list2):
    if isinstance(list1, Token) and list1.type == "list" and isinstance(list2, Token) and list2.type == "list":
        set1 = {(token.value, token.type) for token in list1.value}
        set2 = {(token.value, token.type) for token in list2.value}
        uniqueTokens = [Token(value, type) for value, type in set1.union(set2)]
        return Token(uniqueTokens, "list")
    else:
        error(8100, "Both arguments must be of type list")

    
def date():
    now = datetime.now()
    day = Token(str(now.day), "string")
    month = Token(str(now.month), "string")
    year = Token(str(now.year), "string")

    return Token([day, month, year], "list")


def time():
    now = datetime.now()
    hour = Token(str(now.hour), "string")
    minute = Token(str(now.minute), "string")
    second = Token(str(now.second), "string")

    return Token([hour, minute, second], "list")


def env():
    environ = {Token(key, "string"): Token(value, "string") for key, value in dict(os.environ).items()}
    return Token(environ, "dict")

def uid():
    user_id = os.getuid()
    return Token(str(user_id), "string")

def gid():
    group_id = os.getgid()
    return Token(str(group_id), "string")


def link(source, destination):
    if isinstance(source, Token) and source.type == "string" and isinstance(destination, Token) and destination.type == "string":
        try:
            os.symlink(source.value, destination.value)
            return Token("true", "bool")
        except Exception as e:
            return Token("false", "bool")
    else:
        error(8100, "Both source and destination must be of type string")
        

def logname():
    return Token(os.getlogin(), "string")

def pwd():
    return Token(os.getcwd(), "string")

def __sleep__(seconds):
    if isinstance(seconds, Token) and seconds.type in ["float", "int"]:
        try:
            sleepTime = float(seconds.value)
            sleep(sleepTime)
            return Token("true", "bool")
        except ValueError:
            error(8100, "Invalid sleep duration")
    else:
        error(8100, "Seconds must be of type int or float")

def uname():
    systemInfo = platform.uname()
    return Token([Token(systemInfo.system, "string"), Token(systemInfo.node, "string"), Token(systemInfo.release, "string"), Token(systemInfo.version, "string"), Token(systemInfo.machine, "string"), Token(systemInfo.processor, "string")], "list")

def whoami():
    username = os.getlogin()
    return Token(username, "string")
