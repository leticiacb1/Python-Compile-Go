import sys 

INT   = 1
PLUS  = 2
MINUS = 3
EOF   = 0 

class Token():
    '''            
        Exemplo : (1 , INT)  = (value , type)
    '''

    def __init__ (self, _type : str , value : int):
        self._type = _type
        self.value = value

    def __str__(self):
        if (self._type ==  'INT'):
            return  "({0} , 'INT')".format(self.value)

        if (self._type == '+'):
            return  "({0} , PLUS)".format(self._type)  

        if (self._type == '-'):
            return  "({0} , MINUS)".format(self._type)

        if (self._type == ""):
            return  "({0} , EOF)".format(self._type)

class Tokenizer():
    '''
        Responsável por capturar um token (átomo) do texto-fonte
    '''

    def __init__ (self, source : str):
        self.source = source 
        self.position = 0 
        self.next = None

    def selectNext(self):
    '''
        Atualiza a variável next com o próximo token passado
    '''
        
        find_token = False
        
        while(not find_token):
            if(self.source[self.position].isdigit()):
                value_str = ''

                while (self.source[self.position].isdigit()) : 
                    value_str += self.source[self.position]

                    if (self.position == len(self.source)-1 ):
                        break

                    self.position +=1

                self.next = Token(_type = 'INT' , value = int(value_str))
                find_token = True

            elif(self.source[self.position] == '+'):
                self.next = Token(_type = self.source[self.position] , value = PLUS)
                self.position +=1

                find_token = True

            elif(self.source[self.position] == '-'):
                self.next = Token(_type = self.source[self.position] , value = MINUS)
                self.position +=1

                find_token = True

            elif(self.source[self.position] == "\\n"):
                self.next = Token(_type = "" , value = EOF)
                self.position +=1

                find_token = True
            else:
                self.position +=1


def main(string_input):
    
    tokenizer = Tokenizer(string_input)
    
    tokenizer.selectNext()
    print(tokenizer.next)

    tokenizer.selectNext()
    print(tokenizer.next)

    tokenizer.selectNext()
    print(tokenizer.next)

    tokenizer.selectNext()
    print(tokenizer.next)

if __name__ == '__main__':
    #std_input = (sys.argv)[1:]
    
    string_input = '1     -+ 2'
    result = main(string_input)
