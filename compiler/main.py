import sys
from parser import Parser
from prepro import PrePro
from table.symbol_table import SymbolTable

def load_file(filename) -> list[str]:
    with open(filename, "r") as f:
        lines = f.readlines()
    return lines

if __name__ == '__main__':
    
    #Lê o aruqivo passado na linha de comando
    filename = (sys.argv)[1:]
    source_code_lines = load_file(filename[0])

    # Retira comentários
    code = PrePro().pre_pro(source_code_lines)

    # Instancia tabela de simbolos
    table = SymbolTable()

    # Resolve a arvore
    tree = Parser().run(code)
    print(" ===== Fiz a arvore certinho ======")
    result = tree.evaluate(table)
