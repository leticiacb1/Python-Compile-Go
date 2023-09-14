'''
Rode todos os teste utilizando:
    Dentro da pasta compiler:
    > cd .. && cd compiler
    > python3 -m pytest ../test/test_delimiters.py
'''

from compiler.parser.parser import Parser

import unittest
import pytest

class TestParentheses(unittest.TestCase):
    def test_correct_use(self): 
        '''
            Should calculate correct value
        '''
        source_code = '- (-4+ 2)'
        assert Parser().run(source_code).evaluate() == 2

    def test_incorrect_use(self): 
        '''
            Should raise a error
        '''
        with pytest.raises(Exception) as error: 
            source_code = '- (-4+ 2 '
            Parser().run(source_code)  