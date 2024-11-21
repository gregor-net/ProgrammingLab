file = open('test.txt', 'r')

word = []
for riga in file:
    word.extend(riga.split(' '))

for n in word:
    count = 0
    for m in word:
        if n.strip()== m.strip():
            count +=1

    print('{} e presente {}'.format(n.strip(),count))            

file.close()