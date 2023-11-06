from .node import Node
from compiler.constants import operators
from compiler.constants import types
from compiler.errors.operators import InvalidOperators

class UnOp(Node):
    '''
    Operações unárias. Contém um filho
    '''

    def __init__(self, value):
        super().__init__(value)

    def evaluate(self, symbol_table) -> (int, str):
        (child) = self.children

        assert self.value in [
            operators._Type.PLUS,
            operators._Type.MINUS,
            operators._Type.NOT
        ], InvalidOperators(f" [UnOp - Evaluate] Invalid operator type = {self.value}")

        value, _type = child.evaluate(symbol_table)

        if (self.value == operators._Type.PLUS):
            instruction = f'''
                                ; UnOp(value = {self.value})
                                MOV EAX , {value} \n
                            '''
            self.ASM.body += instruction
            return (1)*value, _type

        if (self.value == operators._Type.MINUS):
            instruction = f'''
                                ; UnOp(value =  {self.value})
                                NEG EAX \n
                            '''
            self.ASM.body += instruction
            return (-1)*value, _type

        if (self.value == operators._Type.NOT):
            instruction = f'''
                                ; UnOp(value =  {self.value})
                                MOV EAX , {not value} \n
                            '''
            self.ASM.body += instruction
            return not value, _type
