import re
from constants import delimiters, eof, invalid, number , operators , functions , identifier
from tokens import Tokens, TokenEOF, TokenInvalid , TokenNumber, TokenOperator , TokenDelimiter , TokenFunction, TokenIdentifier

class Tokenizer():
    '''
        Responsável por capturar um token (átomo) do texto-fonte
    '''

    def __init__ (self, source : str):
        self.source = source 
        self.position = 0 
        self.next = Tokens("", 0)

        self.reserved_words = ('println')

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
                elif(self.source[self.position] == operators._Type.EQUAL):
                    self.next = TokenOperator(type = operators._Type.EQUAL , value = operators._Value.EQUAL)
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
                elif(self.source[self.position] == delimiters._Type.END_OF_LINE):
                    self.next = TokenDelimiter(type = delimiters._Type.END_OF_LINE , value = delimiters._Value.END_OF_LINE)
                    self.position +=1
                    break
                elif(self.source[self.position].isalpha()):
                    # Pode ser uma palavra reservada ou um caracter
                    value_str = ''

                    while(self.position < len(self.source) and (re.search(r'[a-zA-Z0-9_]+', self.source[self.position]))):
                        value_str += self.source[self.position]
                        self.position +=1  
                    
                    if value_str in self.reserved_words:
                        # Function
                        self.next = TokenFunction(type = function._Type.PRINTLN , value = function._Value.PRINTLN)
                    else:
                        # Identififer / Variable
                        self.next = TokenIdentifier(type = identifier._Type.IDENTIFIER, value = value_str)

                    break
                elif(self.source[self.position].isspace()):
                    self.position +=1
                else:
                    self.next = TokenInvalid(type = invalid._Type.INVALID , value = invalid._Value.INVALID)
                    self.position +=1
                    break 
