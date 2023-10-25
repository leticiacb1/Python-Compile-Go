from .node import Node
from compiler.constants import operators
from compiler.constants import types

class BinOp(Node):
    '''
    Operações binárias. Contém dois filhos

    True e False agora representado de forma numérica : true(1) , false(0)
    '''

    def __init__(self, value):
        super().__init__(value)

    def evaluate(self, symbol_table) -> (int, int | str):
        if (self.value == operators._Type.PLUS):
            value1 , type1 =  self.children[0].evaluate(symbol_table)
            value2 , type2 =  self.children[1].evaluate(symbol_table)

            if( (type1 == types.INT) and (type2 == types.INT) ):
                return value1 + value2, types.INT

            raise TypeError

        if (self.value == operators._Type.MINUS):
            value1 , type1 = self.children[0].evaluate(symbol_table)
            value2 , type2 = self.children[1].evaluate(symbol_table)

            if ((type1 == types.INT) and (type2 == types.INT)):
                return value1 - value2, types.INT

            raise TypeError

        if (self.value == operators._Type.BAR):
            value1, type1 = self.children[0].evaluate(symbol_table)
            value2, type2 = self.children[1].evaluate(symbol_table)

            if ((type1 == types.INT) and (type2 == types.INT)):
                return value1//value2, types.INT

            raise TypeError

        if (self.value == operators._Type.TIMES):
            value1, type1 = self.children[0].evaluate(symbol_table)
            value2, type2 = self.children[1].evaluate(symbol_table)

            if ((type1 == types.INT) and (type2 == types.INT)):
                return value1 * value2, types.INT

            raise TypeError

        if (self.value == operators._Type.OR):
            value1, type1 = self.children[0].evaluate(symbol_table)
            value2, type2 = self.children[1].evaluate(symbol_table)

            if ((type1 == types.INT) and (type2 == types.INT)):
                if(value1 or value2):   # Booleanos nao inteiros agora:
                    return 1, types.INT
                return 0, types.INT

            raise TypeError

        if (self.value == operators._Type.AND):
            value1, type1 = self.children[0].evaluate(symbol_table)
            value2, type2 = self.children[1].evaluate(symbol_table)

            if ((type1 == types.INT) and (type2 == types.INT)):
                if(value1 and value2):   # Booleanos nao inteiros agora:
                    return 1, types.INT
                return 0, types.INT

            raise TypeError

        if (self.value == operators._Type.BIGGER_THEN):
            value1, type1 = self.children[0].evaluate(symbol_table)
            value2, type2 = self.children[1].evaluate(symbol_table)

            if ((type1 == types.INT) and (type2 == types.INT)):
                if(value1 > value2):   # Booleanos nao inteiros agora:
                    return 1, types.INT
                return 0, types.INT

            raise TypeError

        if (self.value == operators._Type.LESS_THAN):
            value1, type1 = self.children[0].evaluate(symbol_table)
            value2, type2 = self.children[1].evaluate(symbol_table)

            if ((type1 == types.INT) and (type2 == types.INT)):
                if (value1 < value2):  # Booleanos nao inteiros agora:
                    return 1, types.INT
                return 0, types.INT

            raise TypeError

        if (self.value == operators._Type.EQUAL_COMP):
            valor = self.children[0].evaluate(symbol_table) == self.children[1].evaluate(symbol_table)

            value1, type1 = self.children[0].evaluate(symbol_table)
            value2, type2 = self.children[1].evaluate(symbol_table)

            if ((type1 == types.INT) and (type2 == types.INT)):
                if (value1 == value2):  # Booleanos nao inteiros agora:
                    return 1, types.INT
                return 0, types.INT

            raise TypeError

        raise TypeError
