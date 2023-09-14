from constants import delimiters, eof, invalid, number , operators
from tokens import Tokens, TokenEOF, TokenInvalid , TokenNumber, TokenOperator , TokenDelimiter

class Tokenizer():
    '''
        Responsável por capturar um token (átomo) do texto-fonte
    '''

    def __init__ (self, source : str):
        self.source = source 
        self.position = 0 
        self.next = Tokens("", 0)

    def select_next(self):
        '''
            Atualiza a variável next com o próximo token passado
        '''
        
        while(True):

            if(self.position >= len(self.source)):
            
                if(self.next.type != eof._Type.EOF):
                    self.next = TokenEOF(type = eof._Type.EOF , value = eof._Value)
                break

            else:
                if(self.source[self.position].isdigit()):
                    value_str = ''

                    while (self.position < len(self.source) and self.source[self.position].isdigit()): 
                        value_str += self.source[self.position]
                        self.position +=1    
                
                    self.next = TokenNumber(type = number._Type.INT , value = int(value_str))
                    break

                elif(self.source[self.position] == operators._Type.PLUS):
                    self.next = TokenOperator(type = operators._Type.PLUS , value = operators._Value.PLUS)
                    self.position +=1
                    break

                elif(self.source[self.position] == operators._Type.MINUS):
                    self.next = TokenOperator(type = operators._Type.MINUS , value = operators._Value.MINUS)
                    self.position +=1
                    break
                
                elif(self.source[self.position] == operators._Type.TIMES):
                    self.next = TokenOperator(type = operators._Type.TIMES , value = operators._Value.TIMES)
                    self.position +=1
                    break

                elif(self.source[self.position] == operators._Type.BAR):
                    self.next = TokenOperator(type = operators._Type.BAR , value = operators._Value.BAR)
                    self.position +=1
                    break
                elif(self.source[self.position] == delimiters._Type.OPEN_PARENTHESES):
                    self.next = TokenDelimiter(type = delimiters._Type.OPEN_PARENTHESES , value = delimiters._Value.PARENTHESES)
                    self.position +=1
                    break
                elif(self.source[self.position] == delimiters._Type.CLOSE_PARENTHESES):
                    self.next = TokenDelimiter(type = delimiters._Type.CLOSE_PARENTHESES , value = delimiters._Value.PARENTHESES)
                    self.position +=1
                    break
                elif(self.source[self.position].isspace()):
                    self.position +=1
                else:
                    self.next = TokenInvalid(type = invalid._Type.INVALID , value = invalid._Value.INVALID)
                    self.position +=1
                    break 
