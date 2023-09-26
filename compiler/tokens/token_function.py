from tokens import Tokens

class TokenFunction (Tokens):

    def __init__ (self, type : str , value : int):
        super().__init__(type, value)

    def __str__(self) -> str:
        return  "({0} , {1})".format(self.type , self.value)