import sys
from parser import Parser

if __name__ == '__main__':
    source_code = (sys.argv)[1:]
    Parser.run(source_code[0])