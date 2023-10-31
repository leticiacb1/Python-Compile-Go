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
        self.ASM.write(instruction=f"\t; ----- [PRINTLN - EVALUATE]  -----\n")
        expression_result , _type = self.children[0].evaluate(symbol_table)
        self.ASM.write(instruction=f"; > Childrens : {expression_result} -----\n")
        self.ASM.write(instruction=f"PUSH EAX ;\n")
        self.ASM.write(instruction=f"PUSH formatout ;\n")
        self.ASM.write(instruction=f"CALL printf ;\n")
        self.ASM.write(instruction=f"ADD ESP , 8 ;\n")
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

        self.ASM.write(instruction=f"\t; ----- [IF - EVALUATE]  -----\n")
        self.children[0].evaluate(symbol_table)                  # Inicialização
        self.ASM.write(instruction=f"IF_{self.id}: ;\n")
        self.ASM.write(instruction=f"CMP EAX , False ;\n")
        self.ASM.write(instruction=f"JMP ELSE_{self.id} ;\n")

        # Bloco If
        self.children[1].evaluate(symbol_table)    # Bloco if
        self.ASM.write(instruction=f"JMP END_{self.id} ;\n")

        # Bloco Else
        self.ASM.write(instruction=f"ELSE_{self.id}: ; \n")
        if(len(self.children) > 2):
            self.children[2].evaluate(symbol_table) # Bloco else

        # Fim
        self.ASM.write(instruction=f"END_{self.id}: ;\n")

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
        self.ASM.write(instruction=f"\t; ----- [FOR - EVALUATE]  -----\n")
        # self.ASM.write(instruction=f"{self.children[0].evaluate(symbol_table)} ; Inicialização\n")
        self.children[0].evaluate(symbol_table)  # Inicialização

        self.ASM.write(instruction=f"LOOP_{self.id}: ;\n")

        # self.ASM.write(instruction=f"{self.children[1].evaluate(symbol_table)} ; Condição\n")
        self.children[1].evaluate(symbol_table)  # Condição

        self.ASM.write(instruction=f"CMP EAX , False ;\n")
        self.ASM.write(instruction=f"JE EXIT_{self.id} ;\n")

        # self.ASM.write(instruction=f"{self.children[4].evaluate(symbol_table)} ; Bloco de Instruções\n")
        # self.ASM.write(instruction=f"{self.children[3].evaluate(symbol_table)} ; Incremento \n")
        self.children[3].evaluate(symbol_table)  # Bloco de Intruções
        self.children[2].evaluate(symbol_table)  # Incremento

        self.ASM.write(instruction=f"JMP LOOP_{self.id} ; Volta para o loop \n")
        self.ASM.write(instruction=f"EXIT_{self.id}:   ; Saida \n")

        condition  = self.children[1]
        increment  = self.children[2]
        block      = self.children[3]

        value, type = condition.evaluate(symbol_table)
        while value:
            block.evaluate(symbol_table)
            increment.evaluate(symbol_table)

            value, type = condition.evaluate(symbol_table)

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
            self.ASM.write(instruction=f"\t; ----- [SCANLN - EVALUATE]  -----\n")
            self.ASM.write(instruction=f"PUSH scanint ;\n")
            self.ASM.write(instruction=f"PUSH formatin ;\n")
            self.ASM.write(instruction=f"CALL scanf ;\n")
            self.ASM.write(instruction=f"ADD ESP , 8 ;\n")
            self.ASM.write(instruction=f"MOV EAX , DWORD [scanint] ;\n")
            self.ASM.write(instruction=f"MOV [EBP - 4] , EAX ;\n")

            return int(number), types.TYPE_INT

        raise InvalidType(f" [SCANLN - EVALUATE] Only the integer type is accepted in the Scanln function. Tried type: {type(number)}")
