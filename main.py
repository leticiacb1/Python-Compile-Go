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
                self.next = Token(_type = "EOF" , value = EOF)
                self.position +=1

                find_token = True
            else:
                self.position +=1


class Parser():
    tokenizer : object

    def parseExpression(self):
        '''
            Analisa se a sintaxe está aderente a gramática
        '''

        # Primeiro caracter deve ser número !
        if(tokenizer.next.value.isdigit()):
            result = tokenizer.next.value
            tokenizer.selectNext()  # Atualiza ara próximo Token

            while(tokenizer.next._type in ['+','-']):

                if(tokenizer.next._type == '+'):
                    tokenizer.selectNext() 

                    # O próximo deve ser um número:
                    if(tokenizer.next.value.isdigit()):
                        result += tokenizer.next.value
                    else:
                        raise Exception("O próximo token deve ser um número!")

                if(tokenizer.next._type == '-'):
                    tokenizer.selectNext()

                    # O próximo deve ser um número:
                    if(tokenizer.next.value.isdigit()):
                        result -= tokenizer.next.value
                    else:
                        raise Exception("O próximo token deve ser um número!")

            return result # Retorna resultado da operação
        else:
            raise Exception("O primeiro caracter deve ser um número!")


    def run(self, source_code):

        tokenizer  = Tokenizer(source_code)
        # Pega próximo token
        token = tokenizer.selectNext()

        # Resultado da expressão analisada
        result  = self.parseExpression()
            
        # Verifica se o último token é do tipo "EOF"
        if (tokenizer.next._type != "EOF"):
            raise Exception("Algo de errado aconteceu")

        print(f"Resultado : {result}")

if __name__ == '__main__':
    #std_input = (sys.argv)[1:]
    
    source_code = '1     -+ 2'
    Parser().run(source_code)
