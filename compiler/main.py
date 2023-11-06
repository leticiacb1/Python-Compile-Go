import sys
from parser import Parser
from prepro import PrePro
from table.symbol_table import SymbolTable
from compiler.assembler import Assembler

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
    result = tree.evaluate(table)

    # Monta Assembly
    Assembler.write_header(filename[0])
    Assembler.write_body(filename[0])
    Assembler.write_footer(filename[0])
