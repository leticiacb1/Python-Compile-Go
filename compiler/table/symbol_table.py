class SymbolTable:
    '''
    Formato  :
                Nome da variavel  |     Value    |   Type
                --------------------------------------------
                      x                   3          Int

    self.table = {
        "x" : {"value" : 3  , "type" : "int },
    }

    O tipo pode ser "INT" ou "STRING" .
    '''
    def __init__(self):
        self.table = {}

    def getter(self, identifier) -> (int, str):
        return self.table[identifier]["value"], self.table[identifier]["type"]

    def create(self, identifier , _type) -> None:
        self.table[identifier]["type"] = _type
        self.table[identifier]["value"] = None

    def setter(self, identifier, value) -> None:
        self.table[identifier]["value"] = value
