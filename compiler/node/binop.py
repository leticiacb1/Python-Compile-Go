from .node import Node
from constants import types


class BinOp(Node):
    '''
    Operações binárias. Contém dois filhos
    '''

    def __init__(self, value):
        super().__init__(value)

    def evaluate(self):
        if (self.value == type.PLUS):
            return self.children[0].evaluate() + self.children[1].evaluate()

        if (self.value == type.MINUS):
            return self.children[0].evaluate() - self.children[1].evaluate()

        if (self.value == type.BAR):
            return self.children[0].evaluate() // self.children[1].evaluate()

        if (self.value == type.TIMES):
            return self.children[0].evaluate() * self.children[1].evaluate()

        raise TypeError