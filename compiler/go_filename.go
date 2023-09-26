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