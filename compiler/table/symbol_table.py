class SymbolTable():

    def __init__(self):
        self.tabel = {}

    def getter(self, identifier):
        return self.tabel[identifier]

    def setter(self, identifier , value):

        if identifier in self.table.keys():
            self.tabel[identifier] = value
        else:
            self.table.append({identifier : value}) 