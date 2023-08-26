from tokenizer import Tokenizer
from constants.token import (types, values)
from errors.parser import InvalidExpression

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
        if(Parser().tokenizer.next.type == types.INT):
            
            # Inicializa resultado e seleciona próximo token
            result = Parser().tokenizer.next.value
            Parser().tokenizer.selectNext()  

            if(Parser().tokenizer.next.type not in ['+','-']):
                raise InvalidExpression(f"\n Expected operator types | Got '{Parser().tokenizer.next}' after a number\n")

            while(Parser().tokenizer.next.type in ['+','-']):
                
                if(Parser().tokenizer.next.type == types.PLUS):
                    Parser().tokenizer.selectNext() 
                    
                    # O próximo deve ser um número:
                    if(Parser().tokenizer.next.type == types.INT):
                        result += Parser().tokenizer.next.value
                    elif(Parser().tokenizer.next.type == types.INVALID):
                        raise InvalidExpression(f"\n Invalid caracter find : {Parser().tokenizer.next} \n")
                    else:
                        raise InvalidExpression(f"\n Expected number type | Got {Parser().tokenizer.next} after a operator")

                if(Parser().tokenizer.next.type == types.MINUS):
                    Parser().tokenizer.selectNext()
                    
                    # O próximo deve ser um número:
                    if(Parser().tokenizer.next.type == types.MINUS):
                        result -= Parser().tokenizer.next.value
                    elif(Parser().tokenizer.next.type == types.INVALID):
                        raise InvalidExpression(f"\n Invalid caracter find : {Parser().tokenizer.next} \n")
                    else:
                        raise InvalidExpression(f"\n Expected number type | Got {Parser().tokenizer.next} after a operator")

                # Próximo token
                Parser().tokenizer.selectNext()
            
            if(Parser().tokenizer.next.type == types.INVALID):
                # Caso de haver tokens inválidos , como pontuações
                raise InvalidExpression(f"\n Invalid caracter find : {Parser().tokenizer.next} \n")
            else:
                return result 

        else:
            raise InvalidExpression(f"\n Expected number type as first caracter \n")

    @staticmethod
    def run(source_code):
        
        # Instancia tokenizer e seleciona primeiro Token
        Parser().change_atribute_value(source_code)
        Parser().tokenizer.selectNext()
        
        # Resultado da expressão analisada
        result  = Parser().parseExpression()
            
        # Verifica se o último token é do tipo "EOF"
        if (Parser().tokenizer.next.type != "EOF"):
            raise Exception("Algo de errado aconteceu")

        print(f"Resultado : {result}")