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

class If(Node):
    '''
    Função if (Golang).
    Possui 2 or 3 filhos (quando possuimos um else).

                 ________ If__________
               /          |           \
    bool_expression     Block_if      Block_else
    '''

    def __init__(self, value):
        super().__init__(value)

    def evaluate(self, symbol_table):

        conditional = self.children[0]
        block_if    = self.children[1]

        if(conditional.evaluate(symbol_table)):
            block_if.evaluate(symbol_table)
        elif(len(self.children) > 2):
            #Bloco else

            if (not conditional.evaluate(symbol_table)):
                self.children[2].evaluate(symbol_table)