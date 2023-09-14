'''
Rode todos os teste utilizando:
    > pytest test.py
Ou rode um test eindividual utilizando:
    > pytest test.py::TestClass::<method>
'''
from ..errors.parser import InvalidExpression
from ..errors.tokens import InvalidToken
from parser import Parser

class TestSimpleCalculator:
    def sum_with_space(self):
        '''
            Should return a correct sum value
        '''
        source_code = ' 1+2'
        assert Parser().run(source_code) == 3

    def subtraction_with_space(self):
        '''
            Should return a correct subtraction value
        '''
        source_code = ' 3 - 2'
        assert Parser().run(source_code) == 1

    def division_with_space(self):
        '''
            Should return a correct division value
        '''
        source_code = ' 3 / 2'
        assert Parser().run(source_code) == 1

    def times_with_space(self):
        '''
            Should return a correct times value
        '''
        source_code = ' 3 * 2'
        assert Parser().run(source_code) == 6

    def without_operator(self): 
        '''
            Should raise a error | Without operator
        '''
        with pytest.raises(InvalidExpression) as error: 
            source_code = ' 3  2' 
            Parser().run(source_code)  
        assert str(error.value) == f"\n Expected operator types after a number\n"

    def invalid_caracter(self): 
        '''
            Should raise a error | Invalid Caracter
        '''
        with pytest.raises(InvalidExpression) as error: 
            source_code = ' 1 ,+ 1' 
            Parser().run(source_code)  
        assert str(error.value) == f"\n Invalid caracter find : {Parser().tokenizer.next} \n"

    def just_operators(self): 
        '''
            Should raise a error | Just operators
        '''
        with pytest.raises(InvalidExpression) as error: 
            source_code = ' 1 +++1 ' 
            Parser().run(source_code)  
        assert str(error.value) == f"\n Expected number type | Got {Parser().tokenizer.next} after a operator"

    def sum_sub_correct_value(self): 
        '''
            Should calculate correct value
        '''
        source_code = ' 789 +345 - 123'
        assert Parser().run(source_code) == 1011

    def sum_sub_div_times_correct_value(self): 
        '''
            Should calculate correct value
        '''
        source_code = '2/2 + (4*2+1) -4'
        assert Parser().run(source_code) == 6

class TestUnaryOperators:
    def minus_minus(self): 
        '''
            Should calculate correct value
        '''
        source_code = '- -4'
        assert Parser().run(source_code) == 4

    def plus_plus(self): 
        '''
            Should calculate correct value
        '''
        source_code = '+ +4'
        assert Parser().run(source_code) == 4

    def plus_minus(self): 
        '''
            Should calculate correct value
        '''
        source_code = '+ -4'
        assert Parser().run(source_code) == -4

    def calculate_expression(self): 
        '''
            Should calculate correct value
        '''
        source_code = '+--2/2 + (4*2+1)'
        assert Parser().run(source_code) == 10

class TestParentheses:
    def correct_use(self): 
        '''
            Should calculate correct value
        '''
        source_code = '- (-4+ 2)'
        assert Parser().run(source_code) == 2

    def incorrect_use(self): 
        '''
            Should raise a error
        '''
        with pytest.raises(InvalidExpression) as error: 
            source_code = '- (-4+ 2 '
            Parser().run(source_code)  

        assert str(error.value) == f"\n Expected close parentheses type | Got {Parser().tokenizer.next}"

class TestComments:

    def ignore_comments_correct_value(self):
        '''
            Should calculate correct value
        '''
        source_code = '- (-4+ 2) // Testando ignorar +2'
        assert Parser().run(source_code) == 2

    def ignore_comments_correct_value(self):
        '''
            Should raise error
        '''
        with pytest.raises(InvalidExpression) as error: 
            source_code = '- (-4+ 2 // Testando error )'
            Parser().run(source_code)  

        assert str(error.value) == f"\n Expected close parentheses type | Got {Parser().tokenizer.next}"