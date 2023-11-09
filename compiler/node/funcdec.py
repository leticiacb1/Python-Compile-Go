from .node import Node

class FuncDec(Node):
    '''
    Declaração de função.

    Possui pelo menos 2 filhos:

    Exemplos:
     1 . Declaração com apenas 2 filhos : def main () { ... }                [2 filhos]
     2 . Declaração com mais de 2 filhos : def soma ( x int , y int) { ... } [4 filhos]

            -------------------FuncDec -------------------
           /             |       ...      |               \
       VarDec          Vardec            VardDec         Block
    (declração)          |------ args ------|        (Ação da função)
         |
    identifier

    '''

    def __init__(self, value):
        super().__init__(value)

    def evaluate(self, symbol_table) -> (None, None):
        return None, None
