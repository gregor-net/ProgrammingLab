def uguale(A, B):
    for n in A:
        for m in B:
            if m == n:
                return True
    return False
            
            
print(uguale("aba", "bbb")) #stringhe

print(uguale([1,2,3,4], [5,6,7,4])) #liste