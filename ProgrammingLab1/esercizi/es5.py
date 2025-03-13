with open('test.txt', 'r') as file:
    righe = file.readlines()

with open('unique.txt', 'w') as unique:
    righe_uniche = set()

    for riga in righe:
            if riga not in righe_uniche:
                unique.write(riga)
                righe_uniche.add(riga)      

file.close()
unique.close()