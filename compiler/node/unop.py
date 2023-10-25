from .node import Node
from compiler.constants import operators
from compiler.constants import types

class UnOp(Node):
    '''
    Operações unárias. Contém um filho
    '''

    def __init__(self, value):
        super().__init__(value)

    def evaluate(self, symbol_table) -> (int, str):
        if (self.value == operators._Type.PLUS):
            valor, _type = self.children[0].evaluate(symbol_table)
            return (1)*valor, _type

        if (self.value == operators._Type.MINUS):
            valor, _type = self.children[0].evaluate(symbol_table)
            return (-1)*valor, _type

        if (self.value == operators._Type.NOT):
            valor, _type = self.children[0].evaluate(symbol_table)  # Booleanos devem virar 0 ou 1

             # if (valor): return 0, _type
             # else : return 1, _type
            return not valor, _type

        raise TypeError
