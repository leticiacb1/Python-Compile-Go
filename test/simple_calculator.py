'''
Rode todos os teste utilizando:
    > pytest test.py
Ou rode um test eindividual utilizando:
    > pytest test.py::TestClass::<method>
'''
from ..errors.parser import InvalidExpression
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

    def correct_value(self): 
        '''
            Should calculate correct value
        '''

        source_code = ' 789 +345 - 123'
        assert Parser().run(source_code) == 1011
