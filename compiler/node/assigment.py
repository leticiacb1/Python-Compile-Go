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

        identifier, type1, position = symbol_table.getter(self.children[0].value)
        result_expression, type2 = self.children[1].evaluate(symbol_table)

        if (type1 == type2):

            self.ASM.write(instruction=f"\t; ----- [ASSIGMENT - EVALUATE]  -----\n")
            self.ASM.write(instruction=f"\t; > Childrens : {identifier} e {result_expression}\n")
            self.ASM.write(instruction=f"MOV EAX , {result_expression} ;\n")
            self.ASM.write(instruction=f"MOV[EBP - {position}], EAX ;\n")

            symbol_table.setter(self.children[0].value, result_expression)
        else:
            raise IncompatibleTypes(f" [ASSIGMENT - EVALUATE] Setting a value type [{type2}] inconsistent with the variable type [{type1}]")
