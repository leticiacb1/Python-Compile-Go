from tokens import Tokens

class TokenRelational(Tokens):

    def __init__ (self, type : str , value : int):
        super().__init__(type, value)

    def __str__(self):
        if (self.type == '=='):
            return  "({0} , 'EQUAL_COMPARISON')".format(self.type)

        if (self.type == '>'):
            return  "({0} , 'BIGGER_THEN')".format(self.type)

        if (self.type == '<'):
            return  "({0} , 'LESS_THAN')".format(self.type)