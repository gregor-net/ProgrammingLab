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
                        try:
                            l2[1] = float(l2[1])
                        except ValueError:
                            print(f"Skipping non-numeric value: {l2[1]}")
                        else:
                            lista.append(l2[1])
        file.close()
        return lista
    
class Model():
    def fit(self, data):
        raise NotImplementedError('Metodo non implementato')
    def predict(self, data):
        raise NotImplementedError('Metodo non implementato')

class TrendModel(Model):
    def __init__(self, window = 3):
        self.window = window
        
        
    def compute_avg_variation(self,data):
        prev_value = None
        variazioni = []
        
        if not isinstance(data, list):
            raise TypeError("I dati devono essere delle liste")
        if len(data)<=2:
            raise ValueError('dobbiamo avere almeno due mesi')
        
        for item in data:
            if prev_value is not None:
                variazioni.append(item - prev_value)
            prev_value = item
        media_var = sum(variazioni) / len(variazioni)
        return media_var
        
    def predict(self, data):
        prediction = data[-1] + self.compute_avg_variation(data)
        return prediction
    
class FitTrendModel(TrendModel):
    def __init__(self, window = 3):
        super().__init__(window)
       
    def fit(self, data):
        self.historical_avg_variation  = super().compute_avg_variation(data)
    
    def predict(self, data):
        prediction = data[-1] + (self.compute_avg_variation(data) + self.historical_avg_variation) / 2
        return prediction

    
    
test_data = [50,52,60]   
test_data2 = [8, 19, 31, 41] 
modello = TrendModel()
modello2 = FitTrendModel()
modello3 = TrendModel()

file = CSVFile("shampoo_sales.csv")
print(file)
test_data3 = file.get_data()
print(test_data2)
print(test_data3)

predizione = modello.predict(test_data)
print(predizione)
modello2.fit(test_data2)
predizione2 = modello2.predict(test_data)
print(predizione2)

predizione3 = modello3.predict(test_data3)
print(predizione3)
    
    