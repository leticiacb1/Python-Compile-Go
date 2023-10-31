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

        valueRight, type2 = self.children[1].evaluate(symbol_table)
        self.ASM.write(instruction=f"PUSH EAX  \n")
        valueLeft, type1 = self.children[0].evaluate(symbol_table)
        self.ASM.write(instruction=f"POP EBX  \n")

        if (self.value == operators._Type.PLUS):
            if( (type1 == types.TYPE_INT) and (type2 == types.TYPE_INT) ):
                self.ASM.write(instruction=f"ADD EAX , EBX ; Binop({valueLeft} + {valueRight})\n\n")
                return valueLeft + valueRight, types.TYPE_INT

            raise IncompatibleTypes(f" [Binop - Evaluate] Incompatible Types find in + operation : {type1} + {type2}")

        if (self.value == operators._Type.MINUS):
            if ((type1 == types.TYPE_INT) and (type2 == types.TYPE_INT)):
                self.ASM.write(instruction=f"SUB EAX , EBX ; Binop({valueLeft} - {valueRight}) \n\n")
                return valueLeft - valueRight, types.TYPE_INT

            raise IncompatibleTypes(f" [Binop - Evaluate] Incompatible Types find in - operation : {type1} - {type2}")

        if (self.value == operators._Type.BAR):
            if ((type1 == types.TYPE_INT) and (type2 == types.TYPE_INT)):
                self.ASM.write(instruction=f"DIV EBX ; Binop({valueLeft} / {valueRight}) \n\n")
                return valueLeft//valueRight, types.TYPE_INT

            raise IncompatibleTypes(f" [Binop - Evaluate] Incompatible Types find in / operation : {type1} / {type2}")

        if (self.value == operators._Type.TIMES):
            if ((type1 == types.TYPE_INT) and (type2 == types.TYPE_INT)):
                self.ASM.write(instruction=f"IMUL EAX, EBX ; Binop({valueLeft} * {valueRight}) \n\n")
                return valueLeft * valueRight, types.TYPE_INT

            raise IncompatibleTypes(f" [Binop - Evaluate] Incompatible Types find in * operation : {type1} * {type2}")

        if (self.value == operators._Type.OR):
            if ((type1 == types.TYPE_INT) and (type2 == types.TYPE_INT)):

                self.ASM.write(instruction=f"OR EAX, EBX ; Binop({valueLeft} || {valueRight}) \n\n")
                if(valueLeft or valueRight):
                    return 1, types.TYPE_INT
                return 0, types.TYPE_INT

            raise IncompatibleTypes(f" [Binop - Evaluate] Incompatible Types find in OR operation : {type1} or {type2}")

        if (self.value == operators._Type.AND):
            if ((type1 == types.TYPE_INT) and (type2 == types.TYPE_INT)):

                self.ASM.write(instruction=f"AND EAX, EBX ; Binop({valueLeft} && {valueRight}) \n\n")
                if(valueLeft and valueRight):
                    return 1, types.TYPE_INT
                return 0, types.TYPE_INT

            raise IncompatibleTypes(f" [Binop - Evaluate] Incompatible Types find in AND operation : {type1} and {type2}")

        if (self.value == operators._Type.BIGGER_THEN):
            if (type1 == type2):
                self.ASM.write(instruction=f"CMP EAX, EBX ; Binop({valueLeft} > {valueRight}) \n\n")
                self.ASM.write(instruction=f"JMP binop_jg ; \n")
                if(valueLeft > valueRight):
                    return 1, types.TYPE_INT
                return 0, types.TYPE_INT

            raise IncompatibleTypes(f" [Binop - Evaluate] Incompatible Types find in > operation : {type1} > {type2}")

        if (self.value == operators._Type.LESS_THAN):
            if (type1 == type2):
                self.ASM.write(instruction=f"CMP EAX, EBX ; Binop({valueLeft} < {valueRight}) \n\n")
                self.ASM.write(instruction=f"JMP binop_jl ; \n")
                if (valueLeft < valueRight):
                    return 1, types.TYPE_INT
                return 0, types.TYPE_INT

            raise IncompatibleTypes(f" [Binop - Evaluate] Incompatible Types find in < operation : {type1} < {type2}")

        if (self.value == operators._Type.EQUAL_COMP):
            if (type1 == type2):
                self.ASM.write(instruction=f"CMP EAX, EBX ; Binop({valueLeft} == {valueRight}) \n\n")
                self.ASM.write(instruction=f"JMP binop_je ; \n")
                if (valueLeft == valueRight):
                    return 1, types.TYPE_INT
                return 0, types.TYPE_INT

            raise IncompatibleTypes(f" [Binop - Evaluate] Incompatible Types find in == operation : {type1} == {type2}")

        if(self.value == operators._Type.CONCAT):
            return str(valueLeft) + str(valueRight) , types.TYPE_STR

        raise InvalidType(f" [Binop - Evaluate] Invalid Type find : {self.value}")
