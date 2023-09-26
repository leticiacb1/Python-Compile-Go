from tokens import Tokens

class TokenOperator(Tokens):

    def __init__ (self, type : str , value : int):
        super().__init__(type, value)

    def __str__(self):
        if (self.type == '+'):
            return  "({0} , 'PLUS')".format(self.type)  

        if (self.type == '-'):
            return  "({0} , 'MINUS')".format(self.type)

        if (self.type == '*'):
            return  "({0} , 'TIME')".format(self.type)

        if (self.type == '/'):
            return  "({0} , 'BAR')".format(self.type)

        if (self.type == '='):
            return  "({0} , 'EQUAL')".format(self.type)

        if (self.type == '!'):
            return  "({0} , 'NOT')".format(self.type)

        if (self.type == '&&'):
            return  "({0} , 'AND')".format(self.type)

        if (self.type == '||'):
            return  "({0} , 'OR')".format(self.type)
