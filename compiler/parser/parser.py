from compiler.tokenizer import Tokenizer
from compiler.constants import delimiters, eof, invalid, number, operators, functions, identifier
from compiler.errors.parser import InvalidExpression
from compiler.errors.tokens import InvalidToken
from compiler.node import (IntVal, BinOp, UnOp, NoOp, Identifier, Assigment, Node, Println , Scanln, If , For, Block , Program)


class Parser:
    tokenizer: object = Tokenizer('')

    @classmethod
    def change_atribute_value(cls, source):
        cls.tokenizer = Tokenizer(source)

    @staticmethod
    def parser_assigment() -> Node:

        tokens = Parser().tokenizer

        node_identifier = Identifier(value=tokens.next.value)
        tokens.select_next()

        if (tokens.next.type == operators._Type.EQUAL):

            tokens.select_next()

            bool_expression = Parser().parse_bool_expression()  # Mudo o assigment

            node_assigment = Assigment(value=operators._Type.EQUAL)
            node_assigment.add_child(node_identifier)  # Left
            node_assigment.add_child(bool_expression)  # Right

        else:
            raise InvalidExpression(f"\n [STATEMENT] Expected assigment token type | Got {tokens.next}")

        return node_assigment

    @staticmethod
    def parser_factor() -> Node:
        '''
        Verifica a existencia de operadores unários.
        '''
        tokens = Parser().tokenizer

        if (tokens.next.type == number._Type.INT):

            node = IntVal(value=tokens.next.value)
            tokens.select_next()

            return node

        elif (tokens.next.type == identifier._Type.IDENTIFIER):
            node = Identifier(value=tokens.next.value)

            tokens.select_next()
            return node

        elif (tokens.next.type == operators._Type.PLUS):

            node = UnOp(value=operators._Type.PLUS)
            tokens.select_next()
            child = Parser().parser_factor()

            node.add_child(child)

            return node

        elif (tokens.next.type == operators._Type.MINUS):

            node = UnOp(value=operators._Type.MINUS)
            tokens.select_next()
            child = Parser().parser_factor()

            node.add_child(child)

            return node

        elif (tokens.next.type == operators._Type.NOT):
            node = UnOp(value=operators._Type.NOT)
            tokens.select_next()
            child = Parser().parser_factor()

            node.add_child(child)

            return node

        elif (tokens.next.type == delimiters._Type.OPEN_PARENTHESES):
            tokens.select_next()
            node = Parser().parse_bool_expression()

            if (tokens.next.type == delimiters._Type.CLOSE_PARENTHESES):
                tokens.select_next()
                return node
            else:
                raise InvalidExpression(f"\n [FACTOR] Expected close parentheses type | Got {tokens.next}")

        elif(tokens.next.type == functions._Type.SCANLN):
            tokens.select_next()
            node = Scanln(value = functions._Type.SCANLN)

            if (tokens.next.type == delimiters._Type.OPEN_PARENTHESES):
                tokens.select_next()
                if (tokens.next.type == delimiters._Type.CLOSE_PARENTHESES):
                    tokens.select_next()
                    return node
                else:
                    raise InvalidToken(f"\n [FACTOR] Expected close parentheses type | Got {tokens.next}")
            else:
                raise InvalidToken(f"\n [FACTOR] Expected open parentheses type | Got {tokens.next}")
        else:
            raise InvalidToken(f"\n [FACTOR] Token type recived : {tokens.next}")

    @staticmethod
    def parser_term() -> Node:
        '''
            Analisa se a sintaxe está aderente a gramática.
            Loops de multiplicação e subtração.
        '''

        tokens = Parser().tokenizer

        left_node = Parser().parser_factor()

        while (tokens.next.type in [operators._Type.TIMES, operators._Type.BAR]):

            if (tokens.next.type == operators._Type.TIMES):
                op_node = BinOp(operators._Type.TIMES)
                op_node.add_child(left_node)

                tokens.select_next()

                right_node = Parser().parser_factor()
                op_node.add_child(right_node)

                left_node = op_node

            elif (tokens.next.type == operators._Type.BAR):
                op_node = BinOp(operators._Type.BAR)
                op_node.add_child(left_node)

                tokens.select_next()

                right_node = Parser().parser_factor()
                op_node.add_child(right_node)

                left_node = op_node

            else:
                raise InvalidToken(f"\n [TERM] Token type recived : {tokens.next.type}")

        return left_node

    @staticmethod
    def parser_expression() -> Node:
        '''
            Analisa se a sintaxe está aderente a gramática.
            Loops de soma e subtração.
            Expressões binárias.
        '''
        tokens = Parser().tokenizer

        left_node = Parser().parser_term()

        while (tokens.next.type in [operators._Type.PLUS, operators._Type.MINUS]):

            if (tokens.next.type == operators._Type.PLUS):
                op_node = BinOp(operators._Type.PLUS)
                op_node.add_child(left_node)

                tokens.select_next()

                right_node = Parser().parser_term()
                op_node.add_child(right_node)

                left_node = op_node

            elif (tokens.next.type == operators._Type.MINUS):
                op_node = BinOp(operators._Type.MINUS)
                op_node.add_child(left_node)

                tokens.select_next()

                right_node = Parser().parser_term()
                op_node.add_child(right_node)

                left_node = op_node

            else:
                raise InvalidToken(f"\n [EXPRESSION]Token type recived : {tokens.next.type}")

        return left_node

    @staticmethod
    def parser_rl_expressions() -> Node:
        tokens = Parser().tokenizer

        left_node = Parser().parser_expression()

        while (tokens.next.type in [operators._Type.BIGGER_THEN, operators._Type.EQUAL_COMP , operators._Type.LESS_THAN]):

            if (tokens.next.type == operators._Type.BIGGER_THEN):
                op_node = BinOp(operators._Type.BIGGER_THEN)
                op_node.add_child(left_node)

                tokens.select_next()

                right_node = Parser().parser_expression()
                op_node.add_child(right_node)

                left_node = op_node

            elif (tokens.next.type == operators._Type.LESS_THAN):
                op_node = BinOp(operators._Type.LESS_THAN)
                op_node.add_child(left_node)

                tokens.select_next()

                right_node = Parser().parser_expression()
                op_node.add_child(right_node)

                left_node = op_node

            elif (tokens.next.type == operators._Type.EQUAL_COMP):
                op_node = BinOp(operators._Type.EQUAL_COMP)
                op_node.add_child(left_node)

                tokens.select_next()

                right_node = Parser().parser_expression()
                op_node.add_child(right_node)

                left_node = op_node

            else:
                raise InvalidToken(f"\n [EXPRESSION]Token type recived : {tokens.next.type}")

        return left_node


    @staticmethod
    def parser_bool_term() -> Node:
        tokens = Parser().tokenizer

        left_node = Parser().parser_rl_expressions()

        while (tokens.next.type == operators._Type.AND):

            if (tokens.next.type == operators._Type.AND):
                op_node = BinOp(operators._Type.AND)
                op_node.add_child(left_node)

                tokens.select_next()

                right_node = Parser().parser_rl_expressions()
                op_node.add_child(right_node)

                left_node = op_node

            else:
                raise InvalidToken(f"\n [BOOL TERM EXPRESSION]Token type recived : {tokens.next.type}")

        return left_node

    @staticmethod
    def parse_bool_expression() -> Node:
        '''
            Analisa se a sintaxe está aderente a gramática.
            Loop de OR.
            Expressões binárias.
        '''
        tokens = Parser().tokenizer

        left_node = Parser().parser_bool_term()

        while (tokens.next.type == operators._Type.OR):

            if (tokens.next.type == operators._Type.OR):
                op_node = BinOp(operators._Type.OR)
                op_node.add_child(left_node)

                tokens.select_next()

                right_node = Parser().parser_bool_term()
                op_node.add_child(right_node)

                left_node = op_node

            else:
                raise InvalidToken(f"\n [BOOL EXPRESSION]Token type recived : {tokens.next.type}")

        return left_node

    @staticmethod
    def parser_statement() -> Node:

        tokens = Parser().tokenizer

        if (tokens.next.type == delimiters._Type.END_OF_LINE):
            tokens.select_next()
            return NoOp(value='END_OF_LINE')

        elif (tokens.next.type == identifier._Type.IDENTIFIER):
            return  Parser().parser_assigment()
        elif (tokens.next.type == functions._Type.PRINTLN):
            tokens.select_next()

            if (tokens.next.type == delimiters._Type.OPEN_PARENTHESES):
                tokens.select_next()

                bool_expression = Parser().parse_bool_expression() # bool_expression ?

                node_println = Println(value=functions._Type.PRINTLN)
                node_println.add_child(bool_expression)

                if (tokens.next.type != delimiters._Type.CLOSE_PARENTHESES):
                    raise InvalidExpression(f"\n [STATEMENT] Expected close parentheses type | Got {tokens.next}")
                tokens.select_next()
                return node_println
            else:
                raise InvalidExpression(f"\n [STATEMENT] Expected open parentheses type | Got {tokens.next}")

        elif(tokens.next.type == functions._Type.IF):
            tokens.select_next()

            bool_expression = Parser().parse_bool_expression() # bool_expression ?
            block_if        = Parser().block()                 # Sem select next entre os dois?

            # Nó do tipo if :
            node_if = If(value=functions._Type.IF)
            node_if.add_child(bool_expression)
            node_if.add_child(block_if)

            if(tokens.next.type == functions._Type.ELSE): # Bloco else : 3 filhos
                tokens.select_next()
                block_else = Parser().block()
                node_if.add_child(block_else)

            return node_if
        elif (tokens.next.type == functions._Type.FOR):
            tokens.select_next()
            init_state = Parser().parser_assigment()

            if(tokens.next.type == delimiters._Type.SEMICOLON):
                tokens.select_next()
                condition = Parser().parse_bool_expression()

                if (tokens.next.type == delimiters._Type.SEMICOLON):
                    tokens.select_next()
                    incremet = Parser().parser_assigment()
                    block    = Parser().block()

                    node_for = For(value = functions._Type.FOR)
                    node_for.add_child(init_state)
                    node_for.add_child(condition)
                    node_for.add_child(incremet)
                    node_for.add_child(block)
                    return node_for
                else:
                    raise InvalidToken(f"\n [STATEMENT] Expected semicolon type | Got : {tokens.next.type}")
            else:
                raise InvalidToken(f"\n [STATEMENT] Expected semicolon type | Got : {tokens.next.type}")
        else:
            raise InvalidToken(f"\n [STATEMENT] Token type recived : {tokens.next.type}")

    @staticmethod
    def block() -> Node:

        node_block = Block(value='BLOCK')
        tokens = Parser().tokenizer

        if (tokens.next.type == delimiters._Type.OPEN_KEY):
            tokens.select_next()

            if (tokens.next.type == delimiters._Type.END_OF_LINE):
                tokens.select_next()

                while(tokens.next.type != delimiters._Type.CLOSE_KEY):
                    state = Parser().parser_statement()
                    node_block.add_child(state)
                tokens.select_next() # Consome o parênteses
                return node_block
            else:
                raise InvalidExpression(f"\n [BLOCK] Expected END OF LINE type | Got {tokens.next}")

    @staticmethod
    def program() -> Node:

        node_program = Program(value='PROGRAM')
        tokens = Parser().tokenizer

        while (tokens.next.type != "EOF"):
            state = Parser().parser_statement()
            node_program.add_child(state)

        tokens.select_next()

        return node_program

    @staticmethod
    def run(code):

        # Instancia tokenizer e seleciona primeiro Token
        Parser().change_atribute_value(code)
        Parser().tokenizer.select_next()

        # Resultado da expressão analisada
        tree = Parser().program()

        # Verifica se o último token é do tipo "EOF"
        if (Parser().tokenizer.next.type != "EOF"):
            raise InvalidExpression(f"\n [RUN] Expected EOF type | Got {Parser().tokenizer.next}")

        return tree