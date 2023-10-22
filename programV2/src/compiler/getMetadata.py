import hashlib
from time import time
from platform import platform
from uuid import getnode
from os import path
import json

from src.compiler.errors import error


def getFilehash(fileLocation):
    fileHash = hashlib.sha256()
    with open(fileLocation, 'rb') as file:
        while True:
            chunk = file.read(fileHash.block_size)
            if not chunk:
                break
            fileHash.update(chunk)
    return fileHash.hexdigest()


def getMacAddress() -> str:
    mac = str(hex(getnode()))[2:]
    return ":".join([mac[i*2:i*2+2] for i in range(6)])


def getVersion() -> str:
    try: 
        with open(path.expanduser("~")+"/.nobash/versions.json", "r") as f:
            data = json.load(f)
    except Exception:
        error(2, [])
    try:
        return data["compiler"]
    except Exception:
        error(3, [])


def getData(fileLocation) -> dict:
    data = {}
    data["filehash"] = getFilehash(fileLocation)
    data["compileunixtime"] = str(time())
    data["compiledsystemos"] = platform()
    data["compiledsystemmac"] = getMacAddress()
    data["compilerversion"] = getVersion()
    return data

