from .node import Node

class IntVal(Node):
    '''
    Valor inteiro. Não possui filhos.
    '''

    def __init__(self, value):
        super().__init__(value)

    def evaluate(self, symbol_table) -> int:
        return self.value