def palindromo(parola):
    for i, _ in enumerate(parola):
        if(parola[i] != parola[-(i+1)]):
            return False
    
    return True

def palindromo2(parola):
    #solution prof 1
    for i in range((len(parola))//2):
        if(parola[i] != parola[-(i+1)]):
            return False
    
    return True

def palindromo3(parola):
    #solution prof 2 ottimizzata
    
    if parola == parola[-1::-1]:
        return True
    
    return False


print(palindromo('CIAOOAIC'))
print(palindromo2('CIAOFOAIC'))
print(palindromo3('CIAOFFFOAIC'))