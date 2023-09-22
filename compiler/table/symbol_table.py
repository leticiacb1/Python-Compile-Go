class SymbolTable:

    def __init__(self):
        self.table = {}

    def getter(self, identifier):
        return self.table[identifier]

    def setter(self, identifier , value):
        self.table[identifier] = value 
