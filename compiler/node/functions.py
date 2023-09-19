from .node import Node

class Println(Node):
    '''
    Função println (Golang).
    Possui um filho.

     println
        |
    Expresion

    [IN]  println(Expression)
    [OUT] Expresion_result

    '''

    def __init__(self, value):
        super().__init__(value)

    def evaluate(self, symbol_table):
        expression_result = self.children[0].evaluate(symbol_table)
        print(expression_result)
        return expression_result