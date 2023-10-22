from sys import exit



def error(errorNumber, info=None):
    if info == None:
        print("Exiting: Error nr. "+str(errorNumber))
    try:
        import src.interpreter.globalSGT as globalSGT
        from os import path
        import json 
        with open(path.expanduser("~")+"/.nobash/interpreterErrors.json", "r") as f: 
            errors = json.load(f)
        if isinstance(info, tuple):
            info = list(info)
        info = [str(data) for data in info]
        lineNumber = globalSGT.currentLine.value+1
        error = f"Line: {lineNumber}; "
        error += errors[str(errorNumber)].format(*info)
        print(error)
        exit(errorNumber)
    except Exception as e:
        print("Unable to read 'interpreterErrors.json' in '~/.nobash/'")
        print(f"Found {errorNumber} with following info:", *info)
        exit(errorNumber)