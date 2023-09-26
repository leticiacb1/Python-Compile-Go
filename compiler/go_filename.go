Println(1)
x = 3+6/3   *  2 -+-  +  2*4/2 + 0/1 -((6+ ((4)))/(2)) // Teste // Teste 2
y_1 = 3
y_1 = y_1 + 2
z__ = x + y_1
// Saida final
Println(x)
Println(z__+1)
if x > 2 {
    Println(1)
}else{
    Println(0)
}

for i = 0 ; i < 10 ; i = i + 1 {

    if i < 5 {
        Println(0)
    }

    if i == 5 {
        Println(5)
    }
}

for j = 0 ; j < 10 ; j = j + 1 {
    y = Scanln()
    Println(y)
}

res = 1 || 0
Println(res)
b = 3
c = 1
a = 0
if b == 3 && c == 3 {
    //Não deve printar
    Println(100)
}else{
    if c == 1 && b ==3 {
        // Deve printar
        Println(50)
    }
}

a = 1
b = !a
if !b {
    Println(a)
}