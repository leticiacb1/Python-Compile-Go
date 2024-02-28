from compiler.parser.parser import Parser
from compiler.prepro.prepro import PrePro
from compiler.utils import utils
from compiler.constants import delimiters
from compiler.table.symbol_table import SymbolTable
from compiler.errors.parser import InvalidExpression

import pytest

class TestComments:

    @pytest.mark.usefixtures("capsys")
    def test_ignore_comments_correct_value(self, capsys):
        '''
            Should calculate correct value
        '''

        # Read file
        filename = '../test/inputs/comments/correct_value.go'
        source_code_lines = utils.load_file(filename)

        # Remove comments
        code = PrePro().pre_pro(source_code_lines) + delimiters._Type.END_OF_LINE

        # Symbol table
        table = SymbolTable()

        # Resolve tree
        tree = Parser().run(code)
        result = tree.evaluate(table)

        captured = capsys.readouterr()

        assert captured.out == "2\n"


    def test_ignore_comments_invalid_syntax(self):
        '''
            Should raise error
        '''
            
        # Read file
        filename = '../test/inputs/comments/invalid_syntax.go'
        source_code_lines = utils.load_file(filename)

        # Remove comments
        code = PrePro().pre_pro(source_code_lines) + delimiters._Type.END_OF_LINE

        # Symbol table
        table = SymbolTable()

        with pytest.raises(Exception):

            # Resolve tree
            tree = Parser().run(code)
            result = tree.evaluate(table)