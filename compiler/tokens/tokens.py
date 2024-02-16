from abc import ABC, abstractmethod
from constants import delimiters, operators , functions , specials , types

class Tokens(ABC):
    '''            
        Define caracters da cadeia de string passada.
    '''

    def __init__ (self, type : str , value : int | str):
        self.type = type
        self.value = value

    def __str__(self) -> str :

        if (self.type == operators._Type.PLUS):
            return  "({0} , 'PLUS')".format(self.type)  
        if (self.type == operators._Type.MINUS):
            return  "({0} , 'MINUS')".format(self.type)
        if (self.type == operators._Type.TIMES):
            return  "({0} , 'TIME')".format(self.type)
        if (self.type == operators._Type.BAR):
            return  "({0} , 'BAR')".format(self.type)
        if (self.type == operators._Type.EQUAL):
            return  "({0} , 'EQUAL')".format(self.type)
        if (self.type == operators._Type.EQUAL_COMP):
            return  "({0} , 'COMPARATION')".format(self.type)
        if (self.type == operators._Type.BIGGER_THEN):
            return  "({0} , 'BIGGER THEN')".format(self.type)
        if (self.type == operators._Type.LESS_THAN):
            return  "({0} , 'LESS THEN')".format(self.type)
        if (self.type == operators._Type.NOT):
            return  "({0} , 'NOT')".format(self.type)
        if (self.type == operators._Type.AND):
            return  "({0} , 'AND')".format(self.type)
        if (self.type == operators._Type.OR):
            return  "({0} , 'OR')".format(self.type)
        if (self.type == operators._Type.CONCAT):
            return  "({0} , 'CONCAT')".format(self.type)

        
        if (self.type == delimiters._Type.OPEN_PARENTHESES):
            return  "({0} , 'OPEN_PARENTHESES')".format(self.type)  
        if (self.type == delimiters._Type.CLOSE_PARENTHESES):
            return  "({0} , 'CLOSE_PARENTHESES')".format(self.type)
        if (self.type == delimiters._Type.OPEN_KEY):
            return  "({0} , 'OPEN_KEY')".format(self.type)
        if (self.type == delimiters._Type.CLOSE_KEY):
            return  "({0} , 'CLOSE_KEY')".format(self.type)
        if (self.type == delimiters._Type.SEMICOLON):
            return  "({0} , 'SEMICOLON')".format(self.type)
        if (self.type == delimiters._Type.END_OF_LINE):
            return  "( '\\n', 'END_OF_LINE')"
        if (self.type == delimiters._Type.COMMAN):
            return  "({0} , 'COMMAN')".format(self.type)


        if (self.type in [function._Type.PRINTLN, function._Type.IF, function._Type.ELSE, function._Type.FOR, 
                          function._Type.SCANLN, function._Type.VAR, function._Type.RETURN, function._Type.FUNC]):
            return  "({0} , {1})".format(self.type , self.value)


        if(self.type == specials._Type.VARIABLE_STR):
            return  "({0} , VARIABLE_STR)".format(self.type , self.value)
        if (self.type == specials._Type.VARIABLE_INT):
            return  "({0} , 'VARIABLE_INT')".format(self.value)
        if (self.type == specials._Type.INVALID):
            return  "({0} , INVALID)".format(self.type)
        if (self.type == specials._Type.IDENTIFIER):
            return  "({0} , FUNCTIONS)".format(self.type , self.value)
        if (self.type == specials._Type.EOF):
            return  "({0} , EOF)".format(self.type)
