'''
Rode todos os teste utilizando:
    Dentro da pasta compiler:
    > cd .. && cd compiler
    > python3 -m pytest ../test/test_simple_calculator.py
'''
from compiler.parser.parser import Parser

import unittest
import pytest

class TestSimpleCalculator(unittest.TestCase):
    def test_sum_with_space(self):
        '''
            Should return a correct sum value
        '''
        source_code = ' 1+2'
        assert Parser().run(source_code).evaluate() == 3

    def test_subtraction_with_space(self):
        '''
            Should return a correct subtraction value
        '''
        source_code = ' 3 - 2'
        assert Parser().run(source_code).evaluate() == 1

    def test_division_with_space(self):
        '''
            Should return a correct division value
        '''
        source_code = ' 3 / 2'
        assert Parser().run(source_code).evaluate() == 1

    def test_times_with_space(self):
        '''
            Should return a correct times value
        '''
        source_code = ' 3 * 2'
        assert Parser().run(source_code).evaluate() == 6

    def test_sum_sub_correct_value(self): 
        '''
            Should calculate correct value
        '''
        source_code = ' 789 +345 - 123'
        assert Parser().run(source_code).evaluate() == 1011

    def test_sum_sub_div_times_correct_value(self): 
        '''
            Should calculate correct value
        '''
        source_code = '2/2 + (4*2+1) -4'
        assert Parser().run(source_code).evaluate() == 6

    def test_without_operator(self): 
        '''
            Should raise a error | Without operator
        '''
        with pytest.raises(Exception): 
            source_code = ' 3  2' 
            Parser().run(source_code) 

    def test_invalid_caracter(self): 
        '''
            Should raise a error | Invalid Caracter
        '''
        with pytest.raises(Exception): 
            source_code = ' 1 ,+ 1' 
            Parser().run(source_code) 