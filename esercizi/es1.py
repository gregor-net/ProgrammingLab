file = open('test.txt', 'r')

count = 0
for riga in file:

    element = riga.split(' ')
    #print(element)
    for word in element:
        if word.strip()== 'ciao':
            count +=1
    
print('ciao e presente {}'.format(count))

file.close()