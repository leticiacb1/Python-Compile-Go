class Token():
    '''            
        Exemplo : (1 , INT)  = (value , type)
    '''

    def __init__ (self, type : str , value : int):
        self.type = type
        self.value = value

    def __str__(self):
        if (self.type ==  'INT'):
            return  "({0} , 'INT')".format(self.value)

        if (self.type == '+'):
            return  "({0} , 'PLUS')".format(self.type)  

        if (self.type == '-'):
            return  "({0} , 'MINUS')".format(self.type)

        if (self.type == "EOF"):
            return  "({0} , EOF)".format(self.type)

        if (self.type == "INVALID"):
            return  "({0} , INVALID)".format(self.type)