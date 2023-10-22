from src.interpreter.token import Token
from src.interpreter.errors import error


def pow(x, y):
    nums = ["int", "float"]
    if x.type in nums and y.type in nums:
        return Token(x.value ** y.value, "float")
    error(304, [x.type, y.type])