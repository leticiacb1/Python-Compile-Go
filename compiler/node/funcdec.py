from .node import Node

class FuncDec(Node):
    '''
    Declaração de função.

    Possui n+2 filhos, onde n é o número de argumentos e os 2 filhos obrigatórios é a declaração da função e o seu bloco de execução.

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
