from .node import Node

class Identifier(Node):
    '''
    Valor variável (icógnita  , ex. x , y or z)
    Não possui filhos.
    '''

    def __init__(self, value):
        super().__init__(value)

    def evaluate(self, symbol_table):
        return symbol_table.getter(value)   