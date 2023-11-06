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

        (left, right) = self.children

        value_right, type2 = right.evaluate(symbol_table)
        self.ASM.body += f'''
                PUSH EAX
                '''
        value_left, type1 = left.evaluate(symbol_table)
        self.ASM.body += f'''
                POP EBX
                '''

        if (self.value == operators._Type.PLUS):
            if ((type1 == types.TYPE_INT) and (type2 == types.TYPE_INT)):
                instruction = f'''
                ; Binop({value_left} + {value_right})
                ADD EAX , EBX\n
                '''
                self.ASM.body += instruction

                return value_left + value_right, types.TYPE_INT

            raise IncompatibleTypes(f" [Binop - Evaluate] Incompatible Types find in + operation : {type1} + {type2}")

        if (self.value == operators._Type.MINUS):
            if ((type1 == types.TYPE_INT) and (type2 == types.TYPE_INT)):
                instruction = f'''
               ; Binop({value_left} - {value_right})
                SUB EAX , EBX\n
                '''
                self.ASM.body += instruction

                return value_left - value_right, types.TYPE_INT

            raise IncompatibleTypes(f" [Binop - Evaluate] Incompatible Types find in - operation : {type1} - {type2}")

        if (self.value == operators._Type.BAR):
            if ((type1 == types.TYPE_INT) and (type2 == types.TYPE_INT)):
                instruction = f'''
                ; Binop({value_left} // {value_right})
                IDIV EBX  \n
                '''
                self.ASM.body += instruction

                return value_left // value_right, types.TYPE_INT

            raise IncompatibleTypes(f" [Binop - Evaluate] Incompatible Types find in / operation : {type1} / {type2}")

        if (self.value == operators._Type.TIMES):
            if ((type1 == types.TYPE_INT) and (type2 == types.TYPE_INT)):
                instruction = f'''
                ; Binop({value_left} * {value_right})
                IMUL EAX, EBX  \n
                '''
                self.ASM.body += instruction

                return value_left * value_right, types.TYPE_INT

            raise IncompatibleTypes(f" [Binop - Evaluate] Incompatible Types find in * operation : {type1} * {type2}")

        if (self.value == operators._Type.OR):
            if ((type1 == types.TYPE_INT) and (type2 == types.TYPE_INT)):

                instruction = f'''
                ; Binop({value_left} || {value_right})
                OR EAX, EBX  \n
                '''
                self.ASM.body += instruction

                if (value_left or value_right):
                    return 1, types.TYPE_INT
                return 0, types.TYPE_INT

            raise IncompatibleTypes(f" [Binop - Evaluate] Incompatible Types find in OR operation : {type1} or {type2}")

        if (self.value == operators._Type.AND):
            if ((type1 == types.TYPE_INT) and (type2 == types.TYPE_INT)):

                instruction = f'''
                ; Binop({value_left} && {value_right})
                AND EAX, EBX \n\n
                '''
                self.ASM.body += instruction

                if (value_left and value_right):
                    return 1, types.TYPE_INT
                return 0, types.TYPE_INT

            raise IncompatibleTypes(
                f" [Binop - Evaluate] Incompatible Types find in AND operation : {type1} and {type2}")

        if (self.value == operators._Type.BIGGER_THEN):
            if (type1 == type2):

                instruction = f'''
                ; Binop({value_left} > {value_right})
                CMP EAX, EBX  
                JMP binop_jg  \n
                '''
                self.ASM.body += instruction

                if (value_left > value_right):
                    return 1, types.TYPE_INT
                return 0, types.TYPE_INT

            raise IncompatibleTypes(f" [Binop - Evaluate] Incompatible Types find in > operation : {type1} > {type2}")

        if (self.value == operators._Type.LESS_THAN):
            if (type1 == type2):

                instruction = f'''
                ; Binop({value_left} < {value_right})
                CMP EAX, EBX  
                JMP binop_jl  \n
               '''
                self.ASM.body += instruction

                if (value_left < value_right):
                    return 1, types.TYPE_INT
                return 0, types.TYPE_INT

            raise IncompatibleTypes(f" [Binop - Evaluate] Incompatible Types find in < operation : {type1} < {type2}")

        if (self.value == operators._Type.EQUAL_COMP):
            if (type1 == type2):

                instruction = f'''
                ; Binop({value_left} == {value_right})
                CMP EAX, EBX 
                JMP binop_je \n
               '''
                self.ASM.body += instruction

                if (value_left == value_right):
                    return 1, types.TYPE_INT
                return 0, types.TYPE_INT

            raise IncompatibleTypes(f" [Binop - Evaluate] Incompatible Types find in == operation : {type1} == {type2}")

        if (self.value == operators._Type.CONCAT):
            return str(value_left) + str(value_right), types.TYPE_STR

        raise InvalidType(f" [Binop - Evaluate] Invalid Type find : {self.value}")
