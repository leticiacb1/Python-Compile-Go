# Compiler
Compilador desenvolvido na disciplina de Lógica da Computação , 7° Semestre Engenharia da Computação , INSPER.

### Diagram ⚠️

<img src = 'Diagrama_v2-4.png'>

### EBNF

```bash

EXPRESSION = TERM, { ("+" | "-"), TERM } ;
TERM = FACTOR, { ("*" | "/"), FACTOR } ;
FACTOR = ("+" | "-") FACTOR | "(" EXPRESSION ")" | number ; 

NUMBER = DIGIT , {DIGIT} ; 
DIGIT = 0 | 1 | ... | 9 ;

```
### Test Status 👩‍💻️
![git status](http://3.129.230.99/svg/leticiacb1/Compiler/)
