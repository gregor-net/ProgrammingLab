class CSVFile():
    
    def __init__(self,name):
        try:
            open(name)
        except FileNotFoundError:
            print("Errore: il file inserito non esiste!")
            exit()
        else:
            self.name = name
                     
    def __str__(self):
        return "CSV file name is: {}".format(self.name)
    
    def get_data(self, start = 0, end = None):
        self.start = start
        self.end = end
        if end is not None and start > end:
            print("Error: Start is bigger than end!")
            return []
        file = open(self.name)
        testo = file.read()
        l1 = testo.split("\n")
        lista = []
        for i, item in enumerate(l1):
            if end is not None and start > end:
                break
            if(start <= i):
                start += 1
                if item != "":
                    l2 = item.split(',')
                    if l2[0] != 'Date':
                        lista.append(l2)
        file.close()
        return lista
    
class NumericalCSVFile(CSVFile):
    def __init__(self,name):
        super().__init__(name)
    
    def __str__(self):
        return "Numerical CSV file name is: {}".format(self.name)  
    
    def get_data(self, start = 0, end = None):
        self.start = start
        self.end = end
        data = super().get_data(start, end)
        ndata = []
        for i, row in enumerate(data):
            try:
                row[1] = float(row[1])
            except ValueError:
                ndata.append("Errore: contiene valori non numerici")
            else:
                ndata.append(row)
        return ndata
    
                
    

    
file = CSVFile("shampoo_sales.csv")
print(file)
print(file.get_data(4,6))
Nfile = NumericalCSVFile("shampoo_sales.csv")
print("\n")
print(Nfile)
print(Nfile.get_data())
