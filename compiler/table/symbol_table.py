from compiler.errors.symbol_table import ExistingKey

class SymbolTable:
    '''
    Formato  :
                Nome da variavel  |     Value    |   Type   |    Position (Bytes)
                -----------------------------------------------------------------
                      x                   3          Int             4

    self.table = {
        "x" : (3  , int , 4),
    }

    table = { var : (value , type , position)}

    O tipo pode ser "INT" ou "STRING" .
    O tipo "INT" e "STRING" ocupam 4 bytes de espaço.
    '''
    def __init__(self):
        self.table = {}
        self.n_rows = 0

    def getter(self, identifier) -> (int, str , int):
        return self.table[identifier][0], self.table[identifier][1] , self.table[identifier][2]

    def create(self, identifier: str, _type: str) -> None:
        if(identifier not in self.table.keys()):
            self.table[identifier] = (None, _type, 4 + self.n_rows*4)
            self.n_rows += 1
        else:
            raise ExistingKey(f" [SYMBOL TABLE - CREATE] The passed key [{identifier}] has already been declared.")

    def setter(self, identifier, value) -> None:
        self.table[identifier] = (value, self.table[identifier][1] , self.table[identifier][2])
