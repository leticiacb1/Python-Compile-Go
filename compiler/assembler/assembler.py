class ASM():
    '''
    Classe responsável por escrever o assembly do código.
    '''

    def __init__(self):
        self.filename = "assembler.asm"
        self._write_header()

    def _process_instructions(self, instruction):
        new_instruction = instruction.split('\n')
        new_instruction = [line.lstrip() for line in new_instruction]

        formatted_instruction = '\n'.join(new_instruction)
        return formatted_instruction

    def _write_header(self):
        header = '''
        ; constantes
        SYS_EXIT equ 1
        SYS_READ equ 3
        SYS_WRITE equ 4
        STDIN equ 0
        STDOUT equ 1
        True equ 1
        False equ 0
        
        segment .data
        formatin: db "%d", 0
        formatout: db "%d", 10, 0 ; newline, null terminator
        scanint: times 4 db 0 ; 32-bit integer = 4 bytes
        
        segment .bss ; variáveis
        res RESB 1
        
        section .text
        global main ; linux
        extern scanf ; linux
        extern printf ; linux
        
        ; subrotinas if/while
        binop_je:
            JE binop_true
            JMP binop_false
        binop_jg:
            JG binop_true
            JMP binop_false
        binop_jl:
            JL binop_true
            JMP binop_false
        binop_false:
            MOV EAX, False
            JMP binop_exit
        binop_true:
            MOV EAX, True
        binop_exit:
            RET
            
        main:
        '''

        formatted_header = self._process_instructions(header)
        with open(self.filename, "w") as file:
            file.write(formatted_header)

    def write(self, instruction) -> None:
        formatted_text = self._process_instructions(instruction)
        with open(self.filename, "a") as file:
            file.write(formatted_text)

    def read(self):
        with open(self.filename, "r+") as file:
            print(file.read())
