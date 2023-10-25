from .node import Node
from compiler.constants import types

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

    def evaluate(self, symbol_table) -> None:
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

    def evaluate(self, symbol_table) -> None:

        conditional = self.children[0]
        block_if    = self.children[1]

        if(conditional.evaluate(symbol_table)):
            block_if.evaluate(symbol_table)
        elif(len(self.children) > 2):
            #Bloco else

            if (not conditional.evaluate(symbol_table)):
                self.children[2].evaluate(symbol_table)

class For(Node):
    '''
    Função for (Golang).
    Possui 4 filhos.

                 ________ For ________________
               /          |           \       \
    Init state     condition      increment    block
    '''

    def __init__(self, value):
        super().__init__(value)

    def evaluate(self, symbol_table) -> None:

        init_state = self.children[0].evaluate(symbol_table)
        condition  = self.children[1]
        increment  = self.children[2]
        block      = self.children[3]

        while condition.evaluate(symbol_table):
            block.evaluate(symbol_table)
            increment.evaluate(symbol_table)

class Scanln(Node):
    '''
    Função Scanln (Golang).
    Não possui filhos.
    '''

    def __init__(self, value):
        super().__init__(value)

    def evaluate(self, symbol_table) -> (int, str):
        number_or_str = input()

        # Número ou string
        if(number_or_str.isdigit()):
            return int(number_or_str), types.INT

        return str(number_or_str), types.STR
