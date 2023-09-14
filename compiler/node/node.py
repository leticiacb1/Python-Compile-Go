from abc import ABC, abstractmethod
from typing import Type
 
class Node(ABC):
    
    def __init__(self, value :  int | str ):
        self.value = value
        self.children = []
    
    def add_child(self, child ):
        self.children.append(child)   

        if(len(self.children) > 2):
            raise ValueError     

    @abstractmethod
    def evaluate(self):
        pass