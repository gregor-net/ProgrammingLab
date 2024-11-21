file = open('test.txt', 'r')

dizionario = {}

for riga in file:

    for word in riga.split(' '):

        count = len(word)
        if word[0] not in dizionario or dizionario[word[0]] < count: 
            dizionario[word[0]] = count  

for key, value in dizionario.items():
    print(f"Key: {key}, Value: {value}")         

file.close()