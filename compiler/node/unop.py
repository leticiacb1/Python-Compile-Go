from .node import Node
from compiler.constants import operators

class UnOp(Node):
    '''
    Operações unárias. Contém um filho
    '''

    def __init__(self, value):
        super().__init__(value)

    def evaluate(self, symbol_table) -> int:
        if (self.value == operators._Type.PLUS):
            return (1)*self.children[0].evaluate(symbol_table)

        if (self.value == operators._Type.MINUS):
            return (-1)*self.children[0].evaluate(symbol_table)

        if (self.value == operators._Type.NOT):
            return not self.children[0].evaluate(symbol_table)

        raise TypeError
