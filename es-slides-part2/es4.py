def tipo_t(a, b, c):

    if a + b > c and a + c > b and b + c > a:
        
        if a == b == c:
            return "Equilatero"
        elif a == b or a == c or b == c:
            return "Isoscele"
        else:
            return "Scaleno"
    else:
        return "Non è un triangolo"
    
print(tipo_t(1,2,4))
print(tipo_t(4,4,4))
print(tipo_t(5,4,3))
print(tipo_t(3,3,5))