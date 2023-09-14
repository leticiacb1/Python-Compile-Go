from .node import Node
from constants import types

class UnOp(Node):
    '''
    Operações unárias. Contém um filho
    '''

    def __init__(self, value):
        super().__init__(value)

    def evaluate(self):
        if (self.value == types.PLUS):
            return (1)*self.children[0].evaluate()

        if (self.value == types.MINUS):
            return (-1)*self.children[0].evaluate()

        raise TypeError