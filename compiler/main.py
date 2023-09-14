import sys
from parser import Parser
from prepro import PrePro

if __name__ == '__main__':
    source_code = (sys.argv)[1:]
    code = PrePro().pre_pro(source_code[0])
    tree = Parser.run(code)

    result = tree.evaluate()
    print(result)