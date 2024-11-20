def n_volte(parola, lettera):
    n = 0
    for carattere in parola:
        if(lettera == carattere):
            n += 1
    return n

print(n_volte('ciaaao', 'a'))