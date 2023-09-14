import sys
from parser import Parser
from prepro import PrePro

if __name__ == '__main__':
    
    source_code = (sys.argv)[1:]

    # Retira comentários
    code = PrePro().pre_pro(source_code[0])

    # Resolve a arvore
    tree = Parser.run(code)
    result = tree.evaluate()
    print(result)