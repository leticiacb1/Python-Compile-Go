from .node import Node

class Assigment(Node):
    '''
    Operações de atribuição (=)
    Possui dois filhos. 

            assigment
            /      \
 (identifier)     (Expresion or a value)
     x         =           2      
     
    '''

    def __init__(self, value):
        super().__init__(value)

    def evaluate(self, symbol_table):
        
        # Valor do filho da direita
        result = self.children[1].evaluate(symbol_table)
        symbol_table.setter(value , result)    