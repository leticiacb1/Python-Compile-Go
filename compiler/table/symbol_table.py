class SymbolTable:

    def __init__(self):
        self.table = {}

    def getter(self, identifier) -> int:
        return self.table[identifier]

    def setter(self, identifier , value) -> None:
        self.table[identifier] = value 
