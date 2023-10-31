from .node import Node
from compiler.constants import types

class IntVal(Node):
    '''
    Valor inteiro. Não possui filhos.
    '''

    def __init__(self, value):
        super().__init__(value)

    def evaluate(self, symbol_table) -> (int, str):
        instruction = f"MOV EAX , {self.value} ; Intval(value = {self.value}) \n\n"
        self.ASM.write(instruction=instruction)

        return self.value, types.TYPE_INT
