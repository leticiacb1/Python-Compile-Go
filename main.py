import sys 

from transform_input import transform_input
from create_tree import create_tree

INT   = 1
PLUS  = 2
MINUS = 3
EOF   = 0 

class Token():
    '''            
        Exemplo : (1 , INT)  = (value , type)
    '''

    def __init__ (self, type : str , value : int):
        self.type = type
        self.value = value

    def __str__(self):
        if (self.value.isdigit()):
            return  "({0},INT)".format(self.value)

        if (self.value = PLUS):
            return  "({0},PLUS)".format(self.type)  

        if (self.value = MINUS):
            return  "({0},MINUS)".format(self.type)

        if (self.value = EOF):
            return  "({0},EOF)".format(self.type)

class Tokenizer():
    '''
        Responsável por capturar um token (átomo) do texto-fonte
    '''

    def __init__ (self, source : str):
        self.source = source 
        self.position = None 
        self.next = None

    def selectNext():
        
        value_str = ''
        type_str  = ''

        if(self.source[position].isdigit())

            while (self.source[position].isdigit()) : 
                value_str += self.source[position]
            
            self.next = Token(type = 'INT' , value = int(value_str))
            self.position +=1

        if (self.source[position] == '+'):
            self.next = Token(type = self.source[position] , value = PLUS)
            self.position +=1

        if (self.source[position] == '-'):
            self.next = Token(type = self.source[position] , value = MINUS)
            self.position +=1

        if (self.source[position] == "\\n"):
            self.next = Token(type = "" , value = EOF)
            self.position +=1

def main(string_input):
    
    
    
if __name__ == '__main__':
    std_input = (sys.argv)[1:]
    result = main(std_input[0])

    print(result)
