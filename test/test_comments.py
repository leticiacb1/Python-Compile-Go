'''
Rode todos os teste utilizando:
    Dentro da pasta compiler:
    > cd .. && cd compiler
    > python3 -m pytest ../test/test_comments.py
'''

from compiler.parser.parser import Parser
from compiler.prepro.prepro import PrePro

import unittest
import pytest

class TestComments(unittest.TestCase):

    def test_ignore_comments_correct_value(self):
        '''
            Should calculate correct value
        '''
        source_code = '- (-4+ 2) // Testando ignorar +2'
        code = PrePro().pre_pro(source_code)
        assert Parser().run(code).evaluate() == 2

    def test_ignore_comments_error_1(self):
        '''
            Should raise error
        '''
        with pytest.raises(Exception) as error: 
            source_code = '- (-4+ 2 // Testando error )'
            code = PrePro().pre_pro(code)
            Parser().run(code)  

    def test_ignore_comments_error_2(self):
        '''
            Should raise error
        '''
        with pytest.raises(Exception) as error: 
            source_code = '- -4+ 2 ) // Testando error -1'
            code = PrePro().pre_pro(source_code)
            Parser().run(code)  