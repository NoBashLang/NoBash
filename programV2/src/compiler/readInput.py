from src.compiler.errors import error




def readFile(fileLocation):
    try:
        with open(fileLocation, "r") as f:
            return [line[:-1] if line.endswith("\n") else line for line in f.readlines()] + ["__exit__()"]
    except Exception:
        error(1, [fileLocation])