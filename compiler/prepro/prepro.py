import re

class PrePro:
    '''
    Responsável pelo pré processamento da cadeia. 
    Retirando comentários.
    '''
    @staticmethod
    def filter(code: str) -> str:
        return re.sub(r"\s*//.*", "", code)

    @staticmethod
    def pre_pro(lines_code: list[str]) -> str:
        code = ''
        for line in lines_code:
            code += PrePro().filter(line)
        
        return code 