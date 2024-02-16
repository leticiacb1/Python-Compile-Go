def load_file(filename) -> list[str]:
    '''
        Lê arquivo
    '''
    with open(filename, "r") as f:
        lines = f.readlines()
    return lines

def check_file_extension(filename) -> None:
    '''
        Verifica se o arquivo passado é do tipo Go
    '''
    extension = filename[0].split(".")[-1]
    if extension != "go":
        raise Exception(" [EXTENSION ERROR] Invalid file extension. Expected .go files.")
