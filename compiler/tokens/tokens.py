from abc import ABC, abstractmethod
 
class Tokens(ABC):
    '''            
        Define caracters da cadeia de string passada.
    '''

    def __init__ (self, type : str , value : int | str):
        self.type = type
        self.value = value