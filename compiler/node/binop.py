from .node import Node
from constants import types


class BinOp(Node):
    '''
    Operações binárias. Contém dois filhos
    '''

    def __init__(self, value):
        super().__init__(value)

    def evaluate(self):
        if (self.value == types.PLUS):
            return self.children[0].evaluate() + self.children[1].evaluate()

        if (self.value == types.MINUS):
            return self.children[0].evaluate() - self.children[1].evaluate()

        if (self.value == types.BAR):
            return self.children[0].evaluate() // self.children[1].evaluate()

        if (self.value == types.TIMES):
            return self.children[0].evaluate() * self.children[1].evaluate()

        raise TypeError