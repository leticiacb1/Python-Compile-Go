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

    def evaluate(self, symbol_table) -> None:
        
        # Valor do filho da direita
        result = self.children[1].evaluate(symbol_table)
        symbol_table.setter(self.children[0].value, result)

        # Expression or a value
        result, type1 = self.children[1].evaluate(symbol_table)

        # Type of de identifier
        identifier, type2 = symbol_table.getter(self.children[0].value)

        # It is only possible to set the value if it were of the same type
        if(type1 == type2):
            symbol_table.setter(self.children[0].value, result)
        else:
            raise TypeError
