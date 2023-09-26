from .node import Node
 
class Block(Node):
    '''
    Pode possuir n filhos.
    Seus filhos são retorno do block Statement.

     __________Block______________
    /           |        ...      \
statement   statement          statement

    '''

    def __init__(self, value):
        super().__init__(value)

    def evaluate(self , symbol_table) -> None:
        for child in self.children:
            child.evaluate(symbol_table)
