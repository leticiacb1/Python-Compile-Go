import re

class PrePro:
    '''
    Responsável pelo pré processamento da cadeia. 
    Retirando comentários.
    '''
    @staticmethod
    def filter(code: str):
        return re.sub(r"\s*//.*", "", code)

    @staticmethod
    def pre_pro(code: str):
        code = PrePro().filter(code)
        return code 