from tokens import Tokens

class TokenDelimiter(Tokens):

    def __init__ (self, type : str , value : int):
        super().__init__(type, value)

    def __str__(self):
        if (self.type == '('):
            return  "({0} , 'OPEN_PARENTHESES')".format(self.type)  
        if (self.type == ')'):
            return  "({0} , 'CLOSE_PARENTHESES')".format(self.type)
        if (self.type == "\n"):
            return  "({0} , 'END_OF_LINE')".format(self.type) 
