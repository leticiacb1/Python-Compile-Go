from .node import Node
from constants import operators


class BinOp(Node):
    '''
    Operações binárias. Contém dois filhos
    '''

    def __init__(self, value):
        super().__init__(value)

    def evaluate(self):
        if (self.value == operators._Type.PLUS):
            return self.children[0].evaluate() + self.children[1].evaluate()

        if (self.value == operators._Type.MINUS):
            return self.children[0].evaluate() - self.children[1].evaluate()

        if (self.value == operators._Type.BAR):
            return self.children[0].evaluate() // self.children[1].evaluate()

        if (self.value == operators._Type.TIMES):
            return self.children[0].evaluate() * self.children[1].evaluate()

        raise TypeError