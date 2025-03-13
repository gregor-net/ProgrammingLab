def scambio(B,i,j):
    A = list(B)
    x = A[i]
    A[i] = A[j]
    A[j] = x
    return A

print(scambio('abcdefghijklmnoprstuvz', 3, 20))