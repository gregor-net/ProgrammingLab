class CSVFile():
    
    def __init__(self,name):
        self.name = name
        
        
    def __str__(self):
        return "CSV file name is: {}".format(self.name)
    
    def get_data(self):
        try:
            file = open(self.name, 'r')
            data = []
            for row in file:
                data.append(row.strip().split(","))
                
            return data
        
        except FileNotFoundError:
            return "File non trovato!!" 
        
class NumericalCSVFile(CSVFile):
    def __init__(self,name):
        super().__init__(name)
    
    def __str__(self):
        return "Numerical CSV file name is: {}".format(self.name)  
    
    def get_data(self):
        data = super().get_data()
        ndata = []
        for i, row in enumerate(data):
            if i == 0:
                ndata.append(row)
            else:
                try:
                    row[1] = float(row[1])
                except ValueError:
                    ndata.append("Errore: contiene valori non numerici")
                else:
                    ndata.append(row)
        return ndata
    
    
file = CSVFile("shampoo_sales.csv")
print(file)
Nfile = NumericalCSVFile("shampoo_sales.csv")
print(Nfile)

print(file.get_data())

print(Nfile.get_data())