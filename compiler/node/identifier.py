from .node import Node

class Identifier(Node):
    '''
    Valor variável (icógnita  , ex. x , y or z)
    Não possui filhos.
    '''

    def __init__(self, value):
        super().__init__(value)

    def evaluate(self, symbol_table) -> (int, str):
        value, _type = symbol_table.get_value_type(self.value)
        position = symbol_table.get_position(self.value)

        instruction = f'''
                ; Identifier(value = {self.value})
                MOV EAX , [EBP - {position}]\n
                '''
        self.ASM.body += instruction

        return value, _type
