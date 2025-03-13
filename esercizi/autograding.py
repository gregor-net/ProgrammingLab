def sum_csv(file_name):
    file = open(file_name, 'r')
    total = 0
    for i,row in enumerate(file):
        try:
            row = row.strip().split(',')
            if i == 0:
                continue
            else:
                value = float(row[1])
        except ValueError:
            print("Valore non numerico!")
        else:      
            total += value
    return total

print(sum_csv("shampoo_sales.csv")) 