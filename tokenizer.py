from constants.token import (types, values)
from token import Token

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
        find_invalid = False
        
        while(not find_token and not find_invalid):

            if(self.position >= len(self.source)):
                
                # Caso EOF não tenha sido lançado ainda
                if(self.next.type != types.EOF):
                    self.next = Token(type = types.EOF , value = values.EOF)
                break

            else:
                if(self.source[self.position].isdigit()):
                    value_str = ''

                    while (self.position < len(self.source) and self.source[self.position].isdigit()): 
                        value_str += self.source[self.position]
                        self.position +=1    
                
                    self.next = Token(type = types.INT , value = int(value_str))
                    find_token = True

                elif(self.source[self.position] == types.PLUS):
                    self.next = Token(type = types.PLUS , value = values.PLUS)
                    self.position +=1

                    find_token = True

                elif(self.source[self.position] == types.MINUS):
                    self.next = Token(type = types.MINUS , value = values.MINUS)
                    self.position +=1

                    find_token = True

                elif(self.source[self.position].isspace()):
                    self.position +=1
                else:
                    self.next = Token(type = types.INVALID , value = values.INVALID)
                    self.position +=1
                    
                    find_invalid = True