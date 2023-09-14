from tokens import Tokens

class TokenInvalid (Tokens):

    def __init__ (self, type : str , value : int):
        super().__init__(type, value)

    def __str__(self):
        return  "({0} , INVALID)".format(self.type)