from .node import Node
from compiler.errors.types import IncompatibleTypes

class Assigment(Node):
    '''
    Operações de atribuição (=)
    Possui dois filhos. 

            assigment
            /      \
 (identifier)     (Expresion or a value)
     x         =           2      
     
    '''

    def __init__(self, value):
        super().__init__(value)

    def evaluate(self, symbol_table) -> None:

        (identifier, expression) = self.children
        value , type1 = symbol_table.get_value_type(identifier.value)
        position      = symbol_table.get_position(identifier.value)

        result_expression, type2 = expression.evaluate(symbol_table)

        if (type1 == type2):

            instruction = f'''
                ; Assigment(identifier = {identifier.value} , value = {result_expression})
                MOV[EBP - {position}], EAX \n
                '''
            self.ASM.body += instruction

            symbol_table.setter(identifier.value, result_expression)
        else:
            raise IncompatibleTypes(f" [ASSIGMENT - EVALUATE] Setting a value type [{type2}] inconsistent with the variable type [{type1}]")
