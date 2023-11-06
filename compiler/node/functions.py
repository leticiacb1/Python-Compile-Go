from .node import Node
from compiler.constants import types
from compiler.errors.types import InvalidType

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
        expression_result, _type = self.children[0].evaluate(symbol_table)

        instruction = f'''
                ; Println
                PUSH EAX 
                PUSH formatout 
                CALL printf 
                ADD ESP , 8\n
            '''
        self.ASM.body += instruction

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
        if len(self.children) > 2:
            (condition, block_if, block_else) = self.children
        else:
            (condition, block_if) = self.children

        condition.evaluate(symbol_table)

        instruction = f'''
            IF_{self.id}: 
                CMP EAX , False 
                JMP ELSE_{self.id}
                '''
        self.ASM.body += instruction

        # Bloco If
        block_if.evaluate(symbol_table)
        self.ASM.body += f'''
                JMP EXIT_IF_{self.id}
                '''

        # Bloco Else
        self.ASM.body += f'''
            ELSE_{self.id}:
            '''
        if len(self.children) > 2:
            block_else.evaluate(symbol_table)

        # Fim
        self.ASM.body += f'''
            EXIT_IF_{self.id}: \n
            '''

        # if(condition.evaluate(symbol_table)):
        #     block_if.evaluate(symbol_table)
        # elif(else_present):
        #     if (not condition.evaluate(symbol_table)):
        #         block_else.evaluate(symbol_table)

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

        (init_state, condition, increment, block) = self.children

        init_state.evaluate(symbol_table) # Inicialização
        self.ASM.body += f'''
            LOOP_{self.id}:
            '''
        condition.evaluate(symbol_table)  # Condição

        instruction = f'''
                CMP EAX , False 
                JE EXIT_LOOP_{self.id}
                '''
        self.ASM.body += instruction

        block.evaluate(symbol_table)      # Bloco de Intruções
        increment.evaluate(symbol_table)  # Incremento

        instruction = f'''
                JMP LOOP_{self.id}
            EXIT_LOOP_{self.id}:\n
            '''
        self.ASM.body += instruction

        # value, _ = condition.evaluate(symbol_table)
        # while value:
        #     block.evaluate(symbol_table)
        #     increment.evaluate(symbol_table)
        #
        #     value, _ = condition.evaluate(symbol_table)

class Scanln(Node):
    '''
    Função Scanln (Golan
    Não possui filhos.
    '''

    def __init__(self, value):
        super().__init__(value)

    def evaluate(self, symbol_table) -> (int, str):

        number = input()

        # Número
        if(number.isdigit()):

            instruction = f''' 
                ; Scanln
                PUSH scanint
                PUSH formatin
                CALL scanf
                ADD ESP , 8 
                MOV EAX , DWORD [scanint]
                MOV [EBP - 4] , EAX \n
                '''
            self.ASM.body += instruction

            return int(number), types.TYPE_INT

        raise InvalidType(f" [SCANLN - EVALUATE] Only the integer type is accepted in the Scanln function. Tried type: {type(number)}")
