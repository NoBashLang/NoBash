from src.interpreter.readInput import readFile
from src.interpreter.formatter import format
from src.interpreter.runner import runInstructions
from src.interpreter.errors import error
from sys import argv

import signal
from os.path import basename



def run(fileLocation):
    rawLines = readFile(fileLocation)
    sections = format(rawLines)
    runInstructions(sections)


def keyboardInterrupt(signal, frame):
    error(430)
    

if __name__ == "__main__":
    signal.signal(signal.SIGINT, keyboardInterrupt)
    try: 
        fileLocation = argv[1]
    except Exception as e:
        error(218)
    
    run(fileLocation)

