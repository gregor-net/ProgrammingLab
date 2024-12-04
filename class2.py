class CSVFile():
    
    def __init__(self,name):
        self.name = name
        
        
    def __str__(self):
        return "CSV file name is: {}".format(self.name)
    
    def get_data(self, start = None, end = None):
        try:
            self.start = start
            self.end = end
            file = open(self.name, 'r')
            rows = file.readlines()
            data = []
            if start is None:
                start = 0
            if end is None:
                end = len(rows)
                
            if start > end:
                raise IndexError("Index start is bigger than index end")
            
            for i, row in enumerate(file):
                if(i==0):
                    data.append(row.strip().split(","))
                if(start > end):
                    break
                if(start <= i):
                    data.append(row.strip().split(","))
                    start += 1
                
            return data
        
        except FileNotFoundError:
            return "File non trovato!!" 
        
class NumericalCSVFile(CSVFile):
    def __init__(self,name):
        super().__init__(name)
    
    def __str__(self):
        return "Numerical CSV file name is: {}".format(self.name)  
    
    def get_data(self, start = None, end = None):
        self.start = start
        self.end = end
        data = super().get_data(start, end)
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

print(file.get_data(1,3))

print(Nfile.get_data())