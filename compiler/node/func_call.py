from .node import Node
from compiler.table import FunctionTable, SymbolTable

class FuncCall(Node):
    '''
    Chamada de Função.

               FuncCall
        (value = nome da função)
      /           |  |          \
    BExpression    ...       BExpression


    '''

    def __init__(self, value):
        super().__init__(value)
        self.function_table = FunctionTable
        self.local_table    = SymbolTable()

    def evaluate(self, symbol_table) -> (None, None):
        #                  function_node (FuncDec)
        #                 /          |           \
        #            VarDec         ...          Block
        #          (declaração)      |
        #               |        VarDec(args)
        #           identifier       |
        #                        identifier


        # ---- Argumentos passados para a função no seu "call" ----
        function_name = self.value
        reviced_args  = self.children

        # ---- Consultando declaração da função e os tipos de argumentos esperados ----
        function_node, _type = self.function_table.getter(function_name)
        declaration, *expected_args, block = function_node.children

        # -- Mesma quantidade de argumentos passados e requeridos pela função: ----
        if(len(reviced_args) != len(expected_args)):
            raise Exception(f" [FUNCALL- EVALUATE] Incorrect number of arguments: expected {len(expected_args)} got {len(reviced_args)}")

        # ---- Varrendo argumentos passados e argumentos esperados ----
        for i in range(len(reviced_args)):

            expected_args[i].evaluate(self.local_table)
            identifier   = expected_args[i].children[0]

            recived_value, recived_type = reviced_args[i].evaluate(self.local_table)

            # Settar valor recebido do argumento
            self.local_table.setter(identifier.value, recived_value)

        # Executando o conteúdo da função:
        block.evaluate(self.local_table)







