from constants.token2 import (types, values)
from token2 import Token

class Tokenizer():
    '''
        Responsável por capturar um token (átomo) do texto-fonte
    '''

    def __init__ (self, source : str):
        self.source = source 
        self.position = 0 
        self.next = Token("", 0)

    def select_next(self):
        '''
            Atualiza a variável next com o próximo token passado
        '''
        
        while(True):

            if(self.position >= len(self.source)):
            
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
                    break

                elif(self.source[self.position] == types.PLUS):
                    self.next = Token(type = types.PLUS , value = values.PLUS)
                    self.position +=1
                    break

                elif(self.source[self.position] == types.MINUS):
                    self.next = Token(type = types.MINUS , value = values.MINUS)
                    self.position +=1
                    break
                
                elif(self.source[self.position] == types.TIMES):
                    self.next = Token(type = types.TIMES , value = values.TIMES)
                    self.position +=1
                    break

                elif(self.source[self.position] == types.BAR):
                    self.next = Token(type = types.BAR , value = values.BAR)
                    self.position +=1
                    break
                elif(self.source[self.position == types.OPEN_BRACKET]):
                    self.next = Token(type = types.OPEN_BRACKET , value = values.BRACKET)
                    self.position +=1
                    break
                elif(self.source[self.position == types.CLOSE_BRACKET]):
                    self.next = Token(type = types.CLOSE_BRACKET , value = values.BRACKET)
                    self.position +=1
                    break
                elif(self.source[self.position].isspace()):
                    self.position +=1
                else:
                    self.next = Token(type = types.INVALID , value = values.INVALID)
                    self.position +=1
                    break 
