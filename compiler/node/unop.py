from .node import Node
from constants import types

class UnOp(Node):
    '''
    Operações unárias. Contém um filho
    '''

    def __init__(self, value):
        super().__init__(value)

    def evaluate(self):
        if (self.value == type.PLUS):
            return (1)*self.children[0].evaluate()

        if (self.value == type.MINUS):
            return (-1)*self.children[0].evaluate()

        raise TypeError