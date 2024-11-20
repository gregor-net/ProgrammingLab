def scritto(A):
    lista = []
    dizionario = {
    0: "zero",
    1: "uno",
    2: "due",
    3: "tre",
    4: "quattro",
    5: "cinque",
    6: "sei",
    7: "sette",
    8: "otto",
    9: "nove",
    10: "dieci",
}
    for n in A:
        lista.append((dizionario[n]))
    return lista

print(scritto([0,2,1,10,3,4,6,7,8]))