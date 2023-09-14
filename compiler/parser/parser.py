from tokenizer import Tokenizer
from constants import (types, values)
from errors.parser import InvalidExpression
from node import (IntVal, BinOp, UnOp, Node)

class Parser():

    tokenizer : object = Tokenizer('')

    @classmethod
    def change_atribute_value(cls, source):
        cls.tokenizer = Tokenizer(source)

    @staticmethod
    def parser_factory():
        '''
        Verifica a existencia de operadores unários.
        '''

        if(Parser().tokenizer.next.type == types.INT):
            num_value = Parser().tokenizer.next.value
            node = IntVal(num_value)

            Parser().tokenizer.select_next() 
            
            return node

        elif(Parser().tokenizer.next.type == types.PLUS):
            Parser().tokenizer.select_next()
            
            node = UnOp(types.PLUS)
            child = Parser().parser_factory()  
            
            # Add child
            node.add_child(child)

            return node

        elif(Parser().tokenizer.next.type == types.MINUS):
            Parser().tokenizer.select_next() 

            node = UnOp(types.MINUS)
            child = Parser().parser_factory()  
            
            # Add child
            node.add_child(child)
            
            return node

        elif(Parser().tokenizer.next.type == types.OPEN_PARENTHESES):
            Parser().tokenizer.select_next() 

            node = Parser().parse_expression() 

            if(Parser().tokenizer.next.type == types.CLOSE_PARENTHESES):
                Parser().tokenizer.select_next() 
                return node
            else:
                raise InvalidExpression(f"\n Expected close parentheses type | Got {Parser().tokenizer.next}")

        else:
            raise InvalidExpression(f"\n Invalid token") 

    @staticmethod
    def parser_term() -> Node:
        '''
            Analisa se a sintaxe está aderente a gramática.
            Loops de multiplicação e subtração.
        '''

        left_node = Parser().parser_factory()

        while(Parser().tokenizer.next.type in [types.TIMES , types.BAR]):
            
            if(Parser().tokenizer.next.type == types.TIMES):
                op_node = BinOp(types.TIMES)
                op_node.add_child(left_node)

                Parser().tokenizer.select_next()
                
                right_node = Parser().parser_factory()
                op_node.add_child(right_node)

                left_node = op_node

            elif(Parser().tokenizer.next.type == types.BAR):
                op_node = BinOp(types.BAR)
                op_node.add_child(left_node)

                Parser().tokenizer.select_next()
                
                right_node = Parser().parser_factory()
                op_node.add_child(right_node)

                left_node = op_node

            else:
                raise InvalidExpression(f"\n Invalid token") 


        return left_node
    
    
    @staticmethod
    def parse_expression():
        '''
            Analisa se a sintaxe está aderente a gramática.
            Loops de soma e subtração.
            Expressões binárias.
        '''

        left_node = Parser().parser_term()

        while(Parser().tokenizer.next.type in [types.PLUS , types.MINUS]):
            
            if(Parser().tokenizer.next.type == types.PLUS):
                op_node = BinOp(types.PLUS)
                op_node.add_child(left_node)

                Parser().tokenizer.select_next()
                
                right_node = Parser().parser_term()
                op_node.add_child(right_node)

                left_node = op_node

            elif(Parser().tokenizer.next.type == types.MINUS):
                op_node = BinOp(types.MINUS)
                op_node.add_child(left_node)

                Parser().tokenizer.select_next()
                
                right_node = Parser().parser_term()
                op_node.add_child(right_node)

                left_node = op_node
            
            else:
                raise InvalidExpression(f"\n Invalid token") 

        return left_node

    @staticmethod
    def run(code):

        # Instancia tokenizer e seleciona primeiro Token
        Parser().change_atribute_value(code)
        Parser().tokenizer.select_next()
        
        # Resultado da expressão analisada
        tree  = Parser().parse_expression()
        
        # Verifica se o último token é do tipo "EOF"
        if (Parser().tokenizer.next.type != "EOF"):
            raise InvalidExpression(f"\n Expected EOF type | Got {Parser().tokenizer.next}")

        return tree