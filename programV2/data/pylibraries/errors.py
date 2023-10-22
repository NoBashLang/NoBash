import sys


def error(errorCode: int, extra=None):
    print("found error:", errorCode, "with extra info", extra)
    sys.exit(errorCode)