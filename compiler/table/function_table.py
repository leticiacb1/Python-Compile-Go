from compiler.errors.symbol_table import ExistingKey
from compiler.node import Node

class FunctionTable:
    '''
    Formato  :
                Nome da função |     Nó endereço    |   Type
                --------------------------------------------
                    main                  Node       (Int or str)

    '''

    table = {}

    def getter(function_name : str) -> (Node, str):
        return FunctionTable.table[function_name][0], FunctionTable.table[function_name][1]

    def declare(function_name : str, node: Node, type: str) -> None:
        if function_name not in FunctionTable.table.keys():
            FunctionTable.table[function_name] = (node, type)
        else:
            raise ExistingKey(f" [FUNCTION TABLE - CREATE] The function [{function_name}] has already been declared.")
