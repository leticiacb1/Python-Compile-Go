import sys
from parser import Parser
from prepro import PrePro
from table.symbol_table import SymbolTable
from constants import delimiters
from utils import utils

def main():
    #Lê o arquivo passado na linha de comando
    filename = (sys.argv)[1:]
    utils.check_file_extension(filename)
    source_code_lines = utils.load_file(filename[0])

    # Retira comentários
    code = PrePro().pre_pro(source_code_lines) + delimiters._Type.END_OF_LINE

    # Instancia tabela de simbolos
    table = SymbolTable()

    # Resolve a arvore
    tree = Parser().run(code)
    result = tree.evaluate(table)


if __name__ == '__main__':
    main()