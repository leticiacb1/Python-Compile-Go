from .node import Node
from compiler.constants import operators
from compiler.constants import types
from compiler.errors.types import IncompatibleTypes, InvalidType

class BinOp(Node):
    '''
    Operações binárias. Contém dois filhos

    True e False agora representado de forma numérica : true(1) , false(0)
    '''

    def __init__(self, value):
        super().__init__(value)

    def evaluate(self, symbol_table) -> (int, int | str):

        self.ASM.write(instruction=f"; ----- [BINOP - EVALUATE]  -----\n")
        self.ASM.write(instruction=f"; > Childrens : {print(self.children[0])} e  {print(self.children[1])} -----\n")

        value1, type1 = self.children[0].evaluate(symbol_table)
        self.ASM.write(instruction=f"PUSH EAX ; \n")
        value2, type2 = self.children[1].evaluate(symbol_table)
        self.ASM.write(instruction=f"POP EBX ; \n")

        if (self.value == operators._Type.PLUS):
            if( (type1 == types.TYPE_INT) and (type2 == types.TYPE_INT) ):
                self.ASM.write(instruction=f"ADD EAX , EBX ; \n")
                return value1 + value2, types.TYPE_INT

            raise IncompatibleTypes(f" [Binop - Evaluate] Incompatible Types find in + operation : {type1} + {type2}")

        if (self.value == operators._Type.MINUS):
            if ((type1 == types.TYPE_INT) and (type2 == types.TYPE_INT)):
                self.ASM.write(instruction=f"SUB EAX , EBX ; \n")
                return value1 - value2, types.TYPE_INT

            raise IncompatibleTypes(f" [Binop - Evaluate] Incompatible Types find in - operation : {type1} - {type2}")

        if (self.value == operators._Type.BAR):
            if ((type1 == types.TYPE_INT) and (type2 == types.TYPE_INT)):
                self.ASM.write(instruction=f"DIV EBX ; \n")
                return value1//value2, types.TYPE_INT

            raise IncompatibleTypes(f" [Binop - Evaluate] Incompatible Types find in / operation : {type1} / {type2}")

        if (self.value == operators._Type.TIMES):
            if ((type1 == types.TYPE_INT) and (type2 == types.TYPE_INT)):
                self.ASM.write(instruction=f"IMUL EAX, EBX ; \n")
                return value1 * value2, types.TYPE_INT

            raise IncompatibleTypes(f" [Binop - Evaluate] Incompatible Types find in * operation : {type1} * {type2}")

        if (self.value == operators._Type.OR):
            if ((type1 == types.TYPE_INT) and (type2 == types.TYPE_INT)):

                self.ASM.write(instruction=f"OR EAX, EBX ; \n")
                if(value1 or value2):
                    return 1, types.TYPE_INT
                return 0, types.TYPE_INT

            raise IncompatibleTypes(f" [Binop - Evaluate] Incompatible Types find in OR operation : {type1} or {type2}")

        if (self.value == operators._Type.AND):
            if ((type1 == types.TYPE_INT) and (type2 == types.TYPE_INT)):

                self.ASM.write(instruction=f"AND EAX, EBX ; \n")
                if(value1 and value2):
                    return 1, types.TYPE_INT
                return 0, types.TYPE_INT

            raise IncompatibleTypes(f" [Binop - Evaluate] Incompatible Types find in AND operation : {type1} and {type2}")

        if (self.value == operators._Type.BIGGER_THEN):
            if (type1 == type2):
                self.ASM.write(instruction=f"CMP EAX, EBX ; \n")
                self.ASM.write(instruction=f"JG LABEL ; \n")  # Como fazer aqui no LABEL?
                if(value1 > value2):
                    return 1, types.TYPE_INT
                return 0, types.TYPE_INT

            raise IncompatibleTypes(f" [Binop - Evaluate] Incompatible Types find in > operation : {type1} > {type2}")

        if (self.value == operators._Type.LESS_THAN):
            if (type1 == type2):
                self.ASM.write(instruction=f"CMP EAX, EBX ; \n")
                self.ASM.write(instruction=f"JL LABEL ; \n")  # Como fazer aqui no LABEL?
                if (value1 < value2):
                    return 1, types.TYPE_INT
                return 0, types.TYPE_INT

            raise IncompatibleTypes(f" [Binop - Evaluate] Incompatible Types find in < operation : {type1} < {type2}")

        if (self.value == operators._Type.EQUAL_COMP):
            if (type1 == type2):
                self.ASM.write(instruction=f"CMP EAX, EBX ; \n")
                self.ASM.write(instruction=f"JE LABEL ; \n")  # Como fazer aqui no LABEL?
                if (value1 == value2):
                    return 1, types.TYPE_INT
                return 0, types.TYPE_INT

            raise IncompatibleTypes(f" [Binop - Evaluate] Incompatible Types find in == operation : {type1} == {type2}")

        if(self.value == operators._Type.CONCAT):
            # Como faz o concat ???
            return str(value1) + str(value2) , types.TYPE_STR

        raise InvalidType(f" [Binop - Evaluate] Invalid Type find : {self.value}")
