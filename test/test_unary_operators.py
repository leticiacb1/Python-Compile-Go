'''
Rode todos os teste utilizando:
    Dentro da pasta compiler:
    > cd .. && cd compiler
    > python3 -m pytest ../test/test_unary_operators.py
'''
from compiler.parser.parser import Parser

import unittest
import pytest

class TestUnaryOperators(unittest.TestCase):
    def test_minus_minus(self): 
        '''
            Should calculate correct value
        '''
        source_code = '- -4'
        assert Parser().run(source_code).evaluate() == 4

    def test_plus_plus(self): 
        '''
            Should calculate correct value
        '''
        source_code = '+ +4'
        assert Parser().run(source_code).evaluate() == 4

    def test_plus_minus(self): 
        '''
            Should calculate correct value
        '''
        source_code = '+ -4'
        assert Parser().run(source_code).evaluate() == -4

    def test_calculate_expression(self): 
        '''
            Should calculate correct value
        '''
        source_code = '+--2/2 + (4*2+1)'
        assert Parser().run(source_code).evaluate() == 10