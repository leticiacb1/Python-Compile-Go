from .node import Node
from compiler.constants import types

class IntVal(Node):
    '''
    Valor inteiro. Não possui filhos.
    '''

    def __init__(self, value):
        super().__init__(value)

    def evaluate(self, symbol_table) -> (int, str):
        self.ASM.write(instruction=f"; ----- [INTVAL - EVALUATE]  -----\n")
        self.ASM.write(instruction=f"; > Children : None  -----\n")
        self.ASM.write(instruction=f"MOV EAX , {self.value} ;\n")
        return self.value, types.TYPE_INT
