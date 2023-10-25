from .node import Node
from compiler.constants import operators
from compiler.constants import types

class UnOp(Node):
    '''
        Pode ter 1 ou 2 filhos:

        Exemplo:
            1 filho : var y int
            2 filhos : var x int = 2

          VarDec
        /       \
identifier      Caso possua BoolExpression
    '''

    def __init__(self, value):
        super().__init__(value)

    def evaluate(self, symbol_table) -> (int, str):

        # Possui apenas um filho
        if(len(self.children) == 1):
            identifier , _type = self.children[0].evaluate()
            symbol_table.create(identifier , _type)
        else:
            # Possui dois filhos
            identifier, _type1 = self.children[0].evaluate()
            boolExpression, _type2 = self.children[0].evaluate()

            if(_type1 == _type2):
                symbol_table.create(identifier, _type1)
                symbol_table.setter(identifier, boolExpression)
        raise TypeError
