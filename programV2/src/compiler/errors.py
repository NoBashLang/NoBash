

def error(errorNumber, info):
    try:
        from os import path
        import json 
        with open(path.expanduser("~")+"/.nobash/compilerErrors.json", "r") as f: 
            errors = json.load(f)
        if isinstance(info, tuple):
            info = list(info)
        error = errors[str(errorNumber)].format(*info)
        print(error)
        exit(errorNumber)
    except Exception as e:
        print("Unable to read 'compilerErrors.json' in '~/.nobash/'")
        print(f"Found {errorNumber} with following info:", *info)
        exit(errorNumber)