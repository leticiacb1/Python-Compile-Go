class _Type:
    OPEN_PARENTHESES  = '('
    CLOSE_PARENTHESES = ')'
    OPEN_KEY          = '{'
    CLOSE_KEY         = '}'
    SEMICOLON         = ';'
    END_OF_LINE       = '\n'

class _Value:
    PARENTHESES = 5
    END_OF_LINE = 6
    OPEN_KEY    = 7
    CLOSE_KEY   = 8
    SEMICOLON   = 9