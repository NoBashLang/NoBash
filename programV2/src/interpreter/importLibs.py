from src.interpreter.errors import error

import sys
import importlib
from os import path

pyLibs = {}

def importPyLib(libName, location):
    try:
        location = location.replace("~", path.expanduser("~"))
        if location not in sys.path:
            sys.path.append(location)
        lib = importlib.import_module(libName)
        pyLibs[libName] = lib
    except Exception as e:
        error(11, [libName, e])