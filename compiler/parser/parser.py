from tokenizer import Tokenizer
from constants import delimiters, eof, invalid , number, operators , functions , identifier
from errors.parser import InvalidExpression 
from errors.tokens import InvalidToken
from node import (IntVal, BinOp, UnOp, NoOp, Identifier, Assigment, Node , Println , Block)

class Parser():

    tokenizer : object = Tokenizer('')

    @classmethod
    def change_atribute_value(cls, source):
        cls.tokenizer = Tokenizer(source)

    @staticmethod
    def parser_factor() -> Node:
        '''
        Verifica a existencia de operadores unários.
        '''
        tokens = Parser().tokenizer
        if(tokens.next.type == number._Type.INT):
            num_value = tokens.next.value
            node = IntVal(num_value)

            tokens.select_next() 
            
            return node

        elif(tokens.next.type == identifier._Type.IDENTIFIER):
            node = Identifier(value = tokens.next.value)
            return node

        elif(tokens.next.type == operators._Type.PLUS):
            tokens.select_next()
            
            node = UnOp(operators._Type.PLUS)
            child = Parser().parser_factor()  
            
            # Add child
            node.add_child(child)

            return node

        elif(tokens.next.type == operators._Type.MINUS):
            tokens.select_next() 

            node = UnOp(operators._Type.MINUS)
            child = Parser().parser_factor()  
            
            # Add child
            node.add_child(child)
            
            return node

        elif(tokens.next.type == delimiters._Type.OPEN_PARENTHESES):
            tokens.select_next() 

            node = Parser().parse_expression() 

            if(tokens.next.type == delimiters._Type.CLOSE_PARENTHESES):
                tokens.select_next() 
                return node
            else:
                raise InvalidExpression(f"\n Expected close parentheses type | Got {tokens.next}")

        else:
            raise InvalidToken(f"\n Token type recived : {tokens.next.type}") 

    @staticmethod
    def parser_term() -> Node:
        '''
            Analisa se a sintaxe está aderente a gramática.
            Loops de multiplicação e subtração.
        '''
        tokens = Parser().tokenizer
        left_node = Parser().parser_factor()

        while(tokens.next.type in [operators._Type.TIMES , operators._Type.BAR]):
            
            if(tokens.next.type == operators._Type.TIMES):
                op_node = BinOp(operators._Type.TIMES)
                op_node.add_child(left_node)

                tokens.select_next()
                
                right_node = Parser().parser_factor()
                op_node.add_child(right_node)

                left_node = op_node

            elif(tokens.next.type == operators._Type.BAR):
                op_node = BinOp(operators._Type.BAR)
                op_node.add_child(left_node)

                tokens.select_next()
                
                right_node = Parser().parser_factor()
                op_node.add_child(right_node)

                left_node = op_node

            else:
                raise InvalidToken(f"\n Token type recived : {tokens.next.type}") 

        return left_node
    
    
    @staticmethod
    def parse_expression():
        '''
            Analisa se a sintaxe está aderente a gramática.
            Loops de soma e subtração.
            Expressões binárias.
        '''
        tokens = Parser().tokenizer
        left_node = Parser().parser_term()

        while(tokens.next.type in [operators._Type.PLUS , operators._Type.MINUS]):
            
            if(tokens.next.type == operators._Type.PLUS):
                op_node = BinOp(operators._Type.PLUS)
                op_node.add_child(left_node)

                tokens.select_next()
                
                right_node = Parser().parser_term()
                op_node.add_child(right_node)

                left_node = op_node

            elif(tokens.next.type == operators._Type.MINUS):
                op_node = BinOp(operators._Type.MINUS)
                op_node.add_child(left_node)

                tokens.select_next()
                
                right_node = Parser().parser_term()
                op_node.add_child(right_node)

                left_node = op_node
            
            else:
                raise InvalidToken(f"\n Token type recived : {tokens.next.type}") 

        return left_node

    @staticmethod
    def statement():

        tokens = Parser().tokenizer
        
        if (tokens.next.type == delimiters._Type.END_OF_LINE):
            return  NoOp()
        elif(tokens.next.type == identifier._Type.IDENTIFIER):
            variable = tokens.next.value
            node_var = Identifier(value = variable)

            tokens.select_next()

            if(tokens.next.type == operators._Type.EQUAL):
                node_assigment = Assigment(value = operators._Type.EQUAL)

                tokens.select_next()

                expression = Parser().parse_expression()

                # Add child
                node_assigment.add_child(node_var)   # Left
                node_assigment.add_child(expression) # Right
                
            else:
                raise InvalidExpression(f"\n Expected assigment token type | Got {tokens.next}")

            return node_assigment  # Retorna ??

        elif(tokens.next.type == functions._Type.PRINTLN):
            node_println = Println(value = functions._Type.PRINTLN)

            if(tokens.next.type == delimiters._Type.OPEN_PARENTHESES):
                tokens.select_next() 

                expression = Parser().parse_expression() 

                if(tokens.next.type == delimiters._Type.CLOSE_PARENTHESES):
                    tokens.select_next() 
                else:
                    raise InvalidExpression(f"\n Expected close parentheses type | Got {tokens.next}")

                node_println.add_child(expression)
                return node_println # Retorna ?
        
        else:
            raise InvalidToken(f"\n Token type recived : {tokens.next.type}") 


    @staticmethod
    def block():

        node_block = Block(value = 'BLOCK')
        tokens = Parser().tokenizer

        while(tokens.next.type != "EOF"):
            state = Parser().statement()
            node_block.add_child(state)

        return node_block

    @staticmethod
    def run(code):

        # Instancia tokenizer e seleciona primeiro Token
        Parser().change_atribute_value(code)
        Parser().tokenizer.select_next()

        # Resultado da expressão analisada
        tree  = Parser().block()
        
        # Verifica se o último token é do tipo "EOF"
        if (Parser().tokenizer.next.type != "EOF"):
            raise InvalidExpression(f"\n Expected EOF type | Got {Parser().tokenizer.next}")

        return tree