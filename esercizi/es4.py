file = open('test.txt', 'r')

dizionario = {}

for riga in file:
    riga = riga.replace('!', '.').replace('?', '.')
    frasi = riga.split('.')


    for frase in frasi:
        frase = frase.strip()
        if frase:
            prima_parola = frase.split()[0] 
            if prima_parola not in dizionario:
                dizionario[prima_parola] = 1
            else:
                dizionario[prima_parola] += 1

for key, value in dizionario.items():
    print(f"Key: {key}, Value: {value}")         

file.close()