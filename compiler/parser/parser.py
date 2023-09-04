from tokenizer import Tokenizer
from constants.token2 import (types, values)
from errors.parser import InvalidExpression

class Parser():

    tokenizer : object = Tokenizer('')

    @classmethod
    def change_atribute_value(cls, source):
        cls.tokenizer = Tokenizer(source)

    @staticmethod
    def parser_factory():
        '''
        Verifica a existencia de operadores unitários
        '''

        if(Parser().tokenizer.next.type == types.INT):
            num_value = Parser().tokenizer.next.value
            Parser().tokenizer.select_next() # Busca próximo
            
            return num_value

        elif(Parser().tokenizer.next.type == types.PLUS):
            Parser().tokenizer.select_next() # Busca próximo
            result = Parser().parser_factory()  
            return (1)*result

        elif(Parser().tokenizer.next.type == types.MINUS):
            Parser().tokenizer.select_next() # Busca próximo
            result = Parser().parser_factory()
            return (-1)*result

        elif(Parser().tokenizer.next.type == types.OPEN_PARENTHESES):
            Parser().tokenizer.select_next() # Busca próximo

            result = Parser().parse_expression()      # Quando terminar , verificar se fecha bracket

            if(Parser().tokenizer.next.type == types.CLOSE_PARENTHESES):
                Parser().tokenizer.select_next() # Busca próximo
                return result
            else:
                raise InvalidExpression(f"\n Expected close parentheses type | Got {Parser().tokenizer.next}")

    @staticmethod
    def parser_term():
        '''
            Analisa se a sintaxe está aderente a gramática.
            Loops de multiplicação e subtração.
        '''

        result = Parser().parser_factory()

        while(Parser().tokenizer.next.type in [types.TIMES , types.BAR]):
            
            if(Parser().tokenizer.next.type == types.TIMES):
                Parser().tokenizer.select_next()
                result *= Parser().parser_factory()

            if(Parser().tokenizer.next.type == types.BAR):
                Parser().tokenizer.select_next()
                result //= Parser().parser_factory()

        return result
    
    
    @staticmethod
    def parse_expression():
        '''
            Analisa se a sintaxe está aderente a gramática.
            Loops de soma e subtração.
            Expressões binárias.
        '''

        result = Parser().parser_term()

        while(Parser().tokenizer.next.type in [types.PLUS , types.MINUS]):
            
            if(Parser().tokenizer.next.type == types.MINUS):
                Parser().tokenizer.select_next()
                result -= Parser().parser_term()

            if(Parser().tokenizer.next.type == types.PLUS):
                Parser().tokenizer.select_next()
                result += Parser().parser_term()

        return result

    @staticmethod
    def run(source_code):
        
        # Instancia tokenizer e seleciona primeiro Token
        Parser().change_atribute_value(source_code)
        Parser().tokenizer.select_next()
        
        # Resultado da expressão analisada
        result  = Parser().parse_expression()
        
        # Verifica se o último token é do tipo "EOF"
        if (Parser().tokenizer.next.type != "EOF"):
            raise Exception("Algo de errado aconteceu")

        print(f"Resultado : {result}")