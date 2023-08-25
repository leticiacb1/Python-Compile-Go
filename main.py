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
            return  "({0} , 'PLUS')".format(self._type)  

        if (self._type == '-'):
            return  "({0} , 'MINUS')".format(self._type)

        if (self._type == "EOF"):
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
            
class Parser():

    tokenizer : object = None

    @classmethod
    def change_atribute_value(cls, source):
        cls.tokenizer = Tokenizer(source)

    @staticmethod
    def parseExpression():
        '''
            Analisa se a sintaxe está aderente a gramática
        '''

        #Primeiro caracter deve ser número !
        if(Parser().tokenizer.next._type == 'INT'):
            
            result = Parser().tokenizer.next.value
            Parser().tokenizer.selectNext()  # Atualiza ara próximo Token

            if(Parser().tokenizer.next._type not in ['+','-']):
                raise Exception("O próximo token deve ser um operador!")

            while(Parser().tokenizer.next._type in ['+','-']):
                print(Parser().tokenizer.next._type)
                
                if(Parser().tokenizer.next._type == '+'):
                    Parser().tokenizer.selectNext() 
                    
                    # O próximo deve ser um número:
                    if(Parser().tokenizer.next._type == 'INT'):
                        result += Parser().tokenizer.next.value
                    else:
                        raise Exception("O próximo token deve ser um número!")

                if(Parser().tokenizer.next._type == '-'):
                    Parser().tokenizer.selectNext()
                    
                    # O próximo deve ser um número:
                    if(Parser().tokenizer.next._type == 'INT'):
                        result -= Parser().tokenizer.next.value

                    else:
                        raise Exception("O próximo token deve ser um número!")

                Parser().tokenizer.selectNext()

            return result # Retorna resultado da operação
        else:
            raise Exception("O primeiro caracter deve ser um número!")

    @staticmethod
    def run(source_code):
        
        # Instancia tokenizer e seleciona primeiro Token
        Parser().change_atribute_value(source_code)
        Parser().tokenizer.selectNext()
        
        # Resultado da expressão analisada
        result  = Parser().parseExpression()
            
        # Verifica se o último token é do tipo "EOF"
        print(Parser().tokenizer.next)
        if (Parser().tokenizer.next._type != "EOF"):
            raise Exception("Algo de errado aconteceu")

        print(f"Resultado : {result}")

if __name__ == '__main__':
    source_code = (sys.argv)[1:]
    Parser().run(source_code[0])
