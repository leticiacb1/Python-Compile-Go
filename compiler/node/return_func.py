from .node import Node

class Return(Node):
    '''
    Nó que representa o retorno da função
    Possui um filho.

            Return
              |
        Bool Expression
       (Valor de retorno)
    '''

    def __init__(self, value):
        super().__init__(value)

    def evaluate(self, symbol_table) -> (None, None):
        bool_expression = self.children[0]
        bool_expression.evaluate()
        return None, None