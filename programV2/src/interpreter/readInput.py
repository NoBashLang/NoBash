from src.interpreter.errors import error

def readFile(fileLocation):
    try:
        with open(fileLocation, "r") as file:
            return [line[:-1] if line.endswith("\n") else line for line in file.readlines()]
    except Exception as e:
        error(94, [fileLocation])


        