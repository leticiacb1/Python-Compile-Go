import re

class PrePro:

    @staticmethod
    def _clean_comments(code: str):
        return re.sub(r"\s*//.*", "", code)

    @staticmethod
    def pre_pro(code: str):
        code = self._clean_comments(code)
        return code 