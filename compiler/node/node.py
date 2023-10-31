from abc import ABC, abstractmethod
from compiler.assembler import ASM
from compiler.dataclass import IdCounter

class Node(ABC):
    
    def __init__(self, value :  int | str):
        self.value = value
        self.children = []

        self.id = IdCounter.counter
        IdCounter.counter += 1

        self.ASM = ASM()
    
    def add_child(self, child ):
        self.children.append(child)     

    def __str__(self):
        return  "<Node (value : {0})>".format(self.value)

    @abstractmethod
    def evaluate(self , symbol_table):
        pass