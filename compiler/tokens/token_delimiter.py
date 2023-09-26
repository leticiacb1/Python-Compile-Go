from tokens import Tokens

class TokenDelimiter(Tokens):

    def __init__ (self, type : str , value : int):
        super().__init__(type, value)

    def __str__(self) -> str:
        if (self.type == '('):
            return  "({0} , 'OPEN_PARENTHESES')".format(self.type)  
        if (self.type == ')'):
            return  "({0} , 'CLOSE_PARENTHESES')".format(self.type)
        if (self.type == '{'):
            return  "({0} , 'OPEN_KEY')".format(self.type)
        if (self.type == '}'):
            return  "({0} , 'CLOSE_KEY')".format(self.type)
        if (self.type == ';'):
            return  "({0} , 'SEMICOLON')".format(self.type)
        if (self.type == "\n"):
            return  "( '\\n', 'END_OF_LINE')"
