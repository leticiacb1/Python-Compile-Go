import re
from compiler.constants import delimiters, eof, invalid, number , operators , functions , identifier
from compiler.tokens import Tokens, TokenEOF, TokenInvalid , TokenNumber, TokenOperator , TokenDelimiter , TokenFunction, TokenIdentifier , TokenRelational

class Tokenizer:
    '''
        Responsável por capturar um token (átomo) do texto-fonte
    '''

    def __init__ (self, source : str):
        self.source = source 
        self.position = 0 
        self.next = Tokens("", 0)

        self.reserved_words = {
            'Println': {'type':functions._Type.PRINTLN , 'value': functions._Value.PRINTLN},
            'Scanln': {'type': functions._Type.SCANLN, 'value': functions._Value.SCANLN},
            'for':  {'type': functions._Type.FOR, 'value': functions._Value.FOR},
            'if': {'type': functions._Type.IF, 'value': functions._Value.IF},
            'else': {'type': functions._Type.ELSE, 'value': functions._Value.ELSE}
        }

    def select_next(self) -> None:
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
                        self.position += 1    
                
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

                    if(self.source[self.position+1] == operators._Type.EQUAL):
                        self.next = TokenRelational(type=operators._Type.EQUAL_COMP, value=operators._Value.EQUAL_COMP)
                        self.position += 1
                    else:
                        self.next = TokenOperator(type = operators._Type.EQUAL , value = operators._Value.EQUAL)

                    self.position +=1
                    break
                elif (self.source[self.position] == operators._Type.BIGGER_THEN):
                    self.next = TokenOperator(type=operators._Type.BIGGER_THEN, value=operators._Value.BIGGER_THEN)
                    self.position += 1
                    break
                elif (self.source[self.position] == operators._Type.LESS_THAN):
                    self.next = TokenOperator(type=operators._Type.LESS_THAN, value=operators._Value.LESS_THAN)
                    self.position += 1
                    break
                elif (self.source[self.position] == operators._Type.NOT):
                    self.next = TokenOperator(type=operators._Type.NOT, value=operators._Value.NOT)
                    self.position += 1
                    break
                elif (self.source[self.position] == operators._Type.AND):
                    self.next = TokenOperator(type=operators._Type.AND, value=operators._Value.AND)
                    self.position += 1
                    break
                elif (self.source[self.position] == operators._Type.OR):
                    self.next = TokenOperator(type=operators._Type.OR, value=operators._Value.OR)
                    self.position += 1
                    break
                elif(self.source[self.position] == delimiters._Type.OPEN_PARENTHESES):
                    self.next = TokenDelimiter(type = delimiters._Type.OPEN_PARENTHESES , value = delimiters._Value.PARENTHESES)
                    self.position +=1
                    break
                elif(self.source[self.position] == delimiters._Type.CLOSE_PARENTHESES):
                    self.next = TokenDelimiter(type = delimiters._Type.CLOSE_PARENTHESES , value = delimiters._Value.PARENTHESES)
                    self.position +=1
                    break
                elif (self.source[self.position] == delimiters._Type.OPEN_KEY):
                    self.next = TokenDelimiter(type=delimiters._Type.OPEN_KEY,
                                               value=delimiters._Value.OPEN_KEY)
                    self.position += 1
                    break
                elif (self.source[self.position] == delimiters._Type.CLOSE_KEY):
                    self.next = TokenDelimiter(type=delimiters._Type.CLOSE_KEY,
                                               value=delimiters._Value.CLOSE_KEY)
                    self.position += 1
                    break
                elif(self.source[self.position] == delimiters._Type.END_OF_LINE):
                    self.next = TokenDelimiter(type = delimiters._Type.END_OF_LINE , value = delimiters._Value.END_OF_LINE)
                    self.position +=1
                    break
                elif (self.source[self.position] == delimiters._Type.SEMICOLON):
                    self.next = TokenDelimiter(type=delimiters._Type.SEMICOLON, value=delimiters._Value.SEMICOLON)
                    self.position += 1
                    break
                elif(self.source[self.position].isalpha()):
                    # Pode ser uma palavra reservada ou um caracter
                    value_str = ''

                    while(self.position < len(self.source) and (re.search(r'[a-zA-Z0-9_]+', self.source[self.position]))):
                        value_str += self.source[self.position]
                        self.position +=1  

                    if value_str in self.reserved_words.keys():
                        # Function
                        self.next = TokenFunction(type = self.reserved_words[value_str]['type'] , value = self.reserved_words[value_str]['value'])
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
