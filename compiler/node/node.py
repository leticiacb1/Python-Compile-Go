from abc import ABC, abstractmethod
 
class Node(ABC):
    
    def __init__(self, value :  int | str ):
        self.value = value
        self.children = []
    
    def add_child(self, child ):
        self.children.append(child)     

    @abstractmethod
    def evaluate(self , symbol_table):
        pass