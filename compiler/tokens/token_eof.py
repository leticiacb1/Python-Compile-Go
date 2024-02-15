from tokens import Tokens

class TokenEOF(Tokens):

    def __init__ (self, type : str , value : int):
        super().__init__(type, value)

    def __str__(self) -> str:
        return  "({0} , EOF)".format(self.type)