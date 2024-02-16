import re

from constants import delimiters, operators , functions , specials , types
from tokens import Tokens

class Tokenizer:
    '''
        Responsável por capturar um token (átomo) do texto-fonte
    '''

    def __init__ (self, source : str):
        self.source = source 
        self.position = 0 
        self.next = Tokens("", 0)

        self.reserved_words = {
            'Println': {'type':functions._Type.PRINTLN , 'value': functions._Value},
            'Scanln': {'type': functions._Type.SCANLN, 'value': functions._Value},
            'for':  {'type': functions._Type.FOR, 'value': functions._Value},
            'if': {'type': functions._Type.IF, 'value': functions._Value},
            'else': {'type': functions._Type.ELSE, 'value': functions._Value},
            'var': {'type': functions._Type.VAR , 'value': functions._Value },
            'int': {'type': types._Type.INT, 'value': types._Value},
            'string': {'type': types._Type.STR, 'value': types._Value},
            'return': {'type': functions._Type.RETURN, 'value': functions._Value},
            'func': {'type': functions._Type.FUNC, 'value': functions._Value}
        }

    def select_next(self) -> None:
        '''
            Atualiza a variável next com o próximo token passado
        '''
        
        while(True):

            if(self.position >= len(self.source)):
            
                if(self.next.type != specials._Type.EOF):
                    self.next = Tokens(type = specials._Type.EOF , value = specials._Value)
                break

            else:
                if(self.source[self.position].isdigit()):
                    value_str = ''

                    while (self.position < len(self.source) and self.source[self.position].isdigit()): 
                        value_str += self.source[self.position]
                        self.position += 1    
                
                    self.next = Tokens(type = specials._Type.VARIABLE_INT , value = int(value_str))
                    break

                elif(self.source[self.position] == operators._Type.PLUS):
                    self.next = Tokens(type = operators._Type.PLUS , value = operators._Value)
                    self.position +=1
                    break

                elif(self.source[self.position] == operators._Type.MINUS):
                    self.next = Tokens(type = operators._Type.MINUS , value = operators._Value)
                    self.position +=1
                    break
                
                elif(self.source[self.position] == operators._Type.TIMES):
                    self.next = Tokens(type = operators._Type.TIMES , value = operators._Value)
                    self.position +=1
                    break

                elif(self.source[self.position] == operators._Type.BAR):
                    self.next = Tokens(type = operators._Type.BAR , value = operators._Value)
                    self.position +=1
                    break
                elif(self.source[self.position] == operators._Type.EQUAL):

                    if(self.source[self.position+1] == operators._Type.EQUAL):
                        self.next = Tokens(type=operators._Type.EQUAL_COMP, value=operators._Value)
                        self.position += 1
                    else:
                        self.next = Tokens(type = operators._Type.EQUAL , value = operators._Value)

                    self.position +=1
                    break
                elif (self.source[self.position] == operators._Type.BIGGER_THEN):
                    self.next = Tokens(type=operators._Type.BIGGER_THEN, value=operators._Value)
                    self.position += 1
                    break
                elif (self.source[self.position] == operators._Type.LESS_THAN):
                    self.next = Tokens(type=operators._Type.LESS_THAN, value=operators._Value)
                    self.position += 1
                    break
                elif (self.source[self.position] == operators._Type.NOT):
                    self.next = Tokens(type=operators._Type.NOT, value=operators._Value)
                    self.position += 1
                    break
                elif ( (self.source[self.position] == operators._Type.E) and (self.source[self.position+1] == operators._Type.E)):
                    self.position += 2
                    self.next = Tokens(type=operators._Type.AND, value=operators._Value)
                    break

                elif ((self.source[self.position] == operators._Type.O) and (self.source[self.position+1] == operators._Type.O)):
                    self.position += 2
                    self.next = Tokens(type=operators._Type.OR, value=operators._Value)
                    break

                elif(self.source[self.position] == operators._Type.CONCAT):
                    self.next = Tokens(type=operators._Type.CONCAT, value=operators._Value)
                    self.position += 1
                    break

                elif(self.source[self.position] == delimiters._Type.OPEN_PARENTHESES):
                    self.next = Tokens(type = delimiters._Type.OPEN_PARENTHESES , value = delimiters._Value)
                    self.position +=1
                    break
                elif(self.source[self.position] == delimiters._Type.CLOSE_PARENTHESES):
                    self.next = Tokens(type = delimiters._Type.CLOSE_PARENTHESES , value = delimiters._Value)
                    self.position +=1
                    break
                elif (self.source[self.position] == delimiters._Type.OPEN_KEY):
                    self.next = Tokens(type=delimiters._Type.OPEN_KEY,
                                               value=delimiters._Value)
                    self.position += 1
                    break
                elif (self.source[self.position] == delimiters._Type.CLOSE_KEY):
                    self.next = Tokens(type=delimiters._Type.CLOSE_KEY,
                                               value=delimiters._Value)
                    self.position += 1
                    break
                elif(self.source[self.position] == delimiters._Type.END_OF_LINE):
                    self.next = Tokens(type = delimiters._Type.END_OF_LINE , value = delimiters._Value)
                    self.position +=1
                    break
                elif (self.source[self.position] == delimiters._Type.SEMICOLON):
                    self.next = Tokens(type=delimiters._Type.SEMICOLON, value=delimiters._Value)
                    self.position += 1
                    break
                elif (self.source[self.position] == delimiters._Type.COMMAN):
                    self.next = Tokens(type=delimiters._Type.COMMAN, value=delimiters._Value)
                    self.position += 1
                    break
                elif(self.source[self.position] == delimiters._Type.QUOTATION_MARKS):

                    value_str = ''
                    self.position += 1
                    while(self.source[self.position] != delimiters._Type.QUOTATION_MARKS):
                        value_str += self.source[self.position]
                        self.position += 1

                    self.position += 1
                    self.next = Tokens(type= specials._Type.VARIABLE_STR , value= value_str)

                    break
                elif(self.source[self.position].isalpha()):
                    # Pode ser uma palavra reservada ou um caracter
                    value_str = ''

                    while(self.position < len(self.source) and (re.search(r'[a-zA-Z0-9_]+', self.source[self.position]))):
                        value_str += self.source[self.position]
                        self.position +=1  

                    if value_str in self.reserved_words.keys():
                        # Function
                        self.next = Tokens(type = self.reserved_words[value_str]['type'] , value = self.reserved_words[value_str]['value'])
                    else:
                        # Identififer / Variable
                        self.next = Tokens(type = specials._Type.IDENTIFIER, value = value_str)

                    break
                elif(self.source[self.position].isspace()):
                    self.position +=1
                else:
                    self.next = Tokens(type = invalid._Type.INVALID , value = invalid._Value.INVALID)
                    self.position +=1
                    break 
