class ASM():
    '''
    Classe responsável por escrever o assembly do código.
    '''

    def __init__(self):
        self.filename = "assembler.asm"
        self._write_header()

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
            PUSH EBP ; guarda o base pointer
            MOV EBP, ESP ; estabelece um novo base pointer
            ; código gerado pelo compilador
            PUSH DWORD 0 ; var i int [EBP-4]
            PUSH DWORD 0 ; var n int [EBP-8]
            PUSH DWORD 0 ; var f int [EBP-12]
            PUSH scanint ; endereço de memória de suporte
            PUSH formatin ; formato de entrada (int)
            call scanf
            ADD ESP, 8 ; Remove os argumentos da pilha
            MOV EAX, DWORD [scanint] ; retorna o valor lido em EAX
            MOV [EBP-8], EAX ; n = Scanln()
            MOV EAX, 1
            MOV [EBP-12], EAX ; f = 1
            ; inicialização do loop
            MOV EAX, 2
            MOV [EBP-4], EAX ; i = 2
        
        LOOP_34:
            MOV EAX, 1
            PUSH EAX ; empilha 1
            MOV EAX, [EBP-8] ; recupera n
            POP EBX
            ADD EAX, EBX ; n + 1
            PUSH EAX ; empilha n + 1
        
            ; condicional do loop
            MOV EAX, [EBP-4] ; recupera i
            POP EBX
            CMP EAX, EBX
            CALL binop_jl ; i < n + 1
            CMP EAX, False ; se a condição for falsa, sai
            JE EXIT_34
        
            ; bloco de comandos
            MOV EAX, [EBP-4] ; i
            PUSH EAX ; empilha i
            MOV EAX, [EBP-12] ; f
            POP EBX ; desempilha i
            IMUL EBX ; f * i
            MOV [EBP-12], EAX ; f = f * i
        
            ; incremento
            MOV EAX, 1
            PUSH EAX ; empilha 1
            MOV EAX, [EBP-4]
            POP EBX
            ADD EAX, EBX ; i + 1
            MOV [EBP-4], EAX ; i = i + 1
            JMP LOOP_34
        
        EXIT_34:
            MOV EAX, [EBP-12]
            PUSH EAX ; empilha f
            PUSH formatout ; formato int de saída
            CALL printf ; Printf
            ADD ESP, 8 ; limpa os argumentos
        
            ; interrupção de saída (default)
            POP EBP
            MOV EAX, 1
            INT 0x80\n\n
        '''

        with open(self.filename, "w") as file:
            file.write(header)

    def write(self, instruction) -> None:
        with open(self.filename, "a") as file:
            file.write(instruction)

    def read(self):
        with open(self.filename, "r+") as file:
            print(file.read())
