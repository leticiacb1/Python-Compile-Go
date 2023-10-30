class ASM():
    '''
    Classe responsável por escrever o assembly do código.
    '''

    def __init__(self):
        self.filename = "asm.txt"

    def write(self, instruction) -> None:
        with open(self.filename, "a") as file:
            file.write(instruction)

    def read(self):
        with open(self.filename, "r+") as file:
            print(file.read())
