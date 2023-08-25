class Token():
    '''            
        Exemplo : (1 , INT)  = (value , type)
    '''

    def __init__ (self, _type : str , value : int):
        self._type = _type
        self.value = value

    def __str__(self):
        if (self._type ==  'INT'):
            return  "({0} , 'INT')".format(self.value)

        if (self._type == '+'):
            return  "({0} , 'PLUS')".format(self._type)  

        if (self._type == '-'):
            return  "({0} , 'MINUS')".format(self._type)

        if (self._type == "EOF"):
            return  "({0} , EOF)".format(self._type)