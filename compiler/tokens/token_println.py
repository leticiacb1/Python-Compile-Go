from tokens import Tokens

class TokenIdentifier (Tokens):

    def __init__ (self, type : str , value : int):
        super().__init__(type, value)

    def __str__(self):
        return  "({0} , {1})".format(self.type , self.value)