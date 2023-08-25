from tokenizer import Tokenizer

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

        #Primeiro caracter deve ser número
        if(Parser().tokenizer.next._type == 'INT'):
            
            # Inicializa resultado e seleciona próximo token
            result = Parser().tokenizer.next.value
            Parser().tokenizer.selectNext()  

            if(Parser().tokenizer.next._type not in ['+','-']):
                raise Exception("O próximo token deve ser um operador!")

            while(Parser().tokenizer.next._type in ['+','-']):
                
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

                # Próximo token
                Parser().tokenizer.selectNext()

            return result 
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
        if (Parser().tokenizer.next._type != "EOF"):
            raise Exception("Algo de errado aconteceu")

        print(f"Resultado : {result}")