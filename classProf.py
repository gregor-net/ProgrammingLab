class CSVFile():
    
    def __init__(self,name):
        try:
            open(name)
        except:
            print("Errore: il file inserito non esiste!")
            exit()
        else:
            self.name = name
            
           
    def __str__(self):
        return "CSV file name is: {}".format(self.name)
    
    def get_data(self):
        file = open(self.name)
        testo = file.read()
        l1 = testo.split("\n")
        lista = []
        for item in l1:
            if item != "":
                l2 = item.split(',')
                if l2[0] != 'Date':
                    lista.append(l2)
        file.close()
        return lista
                
    

    
file = CSVFile("shampoo_sales.csv")
print(file)
print(file.get_data())
