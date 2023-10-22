import string
import src.interpreter.errors as errors
import src.interpreter.varsAndFuncs as varsAndFuncs



class Token():
    def __init__(self, value: str, type=None ):
        self.value = value
        self.type = None
        if not type:
            self.detect()
        else:
            self.type = type

    def specialDetect(self):
        self.type = "special"
    
    def __bool__(self):
        if self.type == "bool" and self.value == "false":
            return False
        if self.type == "nonetype":
            return False
        return True

    def detect(self):
        undetected = False
        mainTypes = [int, str, float, bool]
        if type(self.value) not in mainTypes:
            self.specialDetect()
            return
        value = str(self.value).strip()
        if value and not any([lett for lett in value if lett not in string.digits+"."]):
            self.type = "float"
            if "." not in value:
                self.value = int(self.value)
                self.type = "int"
                return
            elif value.count(".") > 1:
                errors.error(21, [value])
            self.value = float(self.value)
            return
        elif value.startswith('"') and value.endswith('"'):
            self.value = value.strip()[1:-1]
            self.type = "string"
            self.value = self.value.replace("&QUOTE", '"')
            return
        elif value == "none":
            self.type = "nonetype"
            return
        elif value in ["true", "false"]:
            self.type = "bool"
            return
        elif varsAndFuncs.varsAndFuncsNameCheck(value):
            _type = varsAndFuncs.isVarOrFunc(value)
            if _type:
                self.type = _type
                return
        errors.error(22, [value])


    def __str__(self):
        def specialString(token):
            if token.type == "string":
                return f'"{token.value}"'
            return str(token)

        if self.type == "list":
            return str("[" + ", ".join(map(specialString, self.value)) + "]")
        elif self.type == "zip":
            return f"{specialString(self.value[0])}: {specialString(self.value[1])}"
        elif self.type == "dict":
            return str("{"+", ".join([f"{specialString(key)}: {specialString(value)}" for key, value in self.value.items()])+"}")
        return str(self.value)


    def __repr__(self):
        value = str(self.value)
        if self.type == "string":
            value = f'"{value}"'
        elif self.type == "zip":
            value = "["+", ".join(map(str, self.value[0:2]))+"]"
        return f"Token({value}, \"{self.type}\")"



"""- Is it an int/float?
	- Does it have only numbers? -> int
	- Does it have only numbers and a fullstop? -> float
- Does it start with and end on quotes? -> string
- Does it start with and end on square/curly braces? -> list/dict
- Is it 'None'? -> nonetype
- Does it start with 'ret'? -> returntype (custom)
- Otherwise, its a function, variable or doesn't exist.
This must be determined and looked up in the corresponding tables during execution."""