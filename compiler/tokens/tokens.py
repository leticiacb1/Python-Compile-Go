from abc import ABC, abstractmethod
 
class Tokens(ABC):
    '''            
        Define caracters da cadeia de string passada.
    '''

    def __init__ (self, type : str , value : int):
        self.type = type
        self.value = value