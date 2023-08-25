from token import Token

INT   = 1
PLUS  = 2
MINUS = 3
EOF   = 0 

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

            if(self.position >= len(self.source)):
                
                # Caso EOF não tenha sido lançado ainda
                if(self.next._type != "EOF"):
                    self.next = Token(_type = 'EOF' , value = EOF)
                break

            else:
                if(self.source[self.position].isdigit()):
                    value_str = ''

                    while (self.position < len(self.source) and self.source[self.position].isdigit()): 
                        value_str += self.source[self.position]
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

                else:
                    self.position +=1