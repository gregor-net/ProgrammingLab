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
            raise ValueError('Start is bigger than end!')
              
        file = open(self.name)
        testo = file.read()
        l1 = testo.split("\n")
        end = len(l1)
        lista = []
        for item in l1[start:end]:
            if item != "":
                l2 = item.split(',')
                if l2[0] != 'Date':
                    try:
                        l2[1] = float(l2[1])
                    except ValueError:
                        print(f"Skipping non-numeric value: {l2[1]}")
                    else:
                        lista.append(l2[1])
            start += 1
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
        
        
    def avg_variation(self,data):
        prev_value = None
        variazioni = []
        
        if not isinstance(data, list):
            raise TypeError("I dati devono essere delle liste")
        if len(data)<2:
            raise ValueError('dobbiamo avere almeno due mesi')
        
        for item in data:
            if prev_value is not None:
                variazioni.append(item - prev_value)
            prev_value = item
        media_var = sum(variazioni) / len(variazioni)
        return media_var
        
    def predict(self, data):
        prediction = data[-1] + self.avg_variation(data)
        return prediction
    
    def evaluate(self,data):
        lunghezza = int(len(data) * 70/100)
        fit_data = data[:lunghezza]
        test_data = data[lunghezza:]
        
        try:
            self.fit(fit_data)
        except NotImplementedError:
            pass
        except Exception as e:
            raise Exception("Il metodo fit e implementato ma ha sollevato un eccezzione: {}".format(e))
            
        error = []
        for i in range(len(test_data)-2):  
            valore_pred = self.predict(test_data[i:i+2])
            error.append(abs(valore_pred - test_data[i+2]))
        mae_error = sum(error)/len(error)
        return mae_error
    
class FitTrendModel(TrendModel):
    def __init__(self, window = 3):
        super().__init__(window)
       
    def fit(self, data):
        self.historical_avg_variation  = super().avg_variation(data)
    
    def predict(self, data):
        prediction = data[-1] + (self.avg_variation(data) + self.historical_avg_variation) / 2
        return prediction
    
    def evaluate(self,data):
        lunghezza = int(len(data) * 70/100)
        fit_data = data[:lunghezza]
        test_data = data[lunghezza:]
        
        try:
            self.fit(fit_data)
        except NotImplementedError:
            pass
        except Exception as e:
            raise Exception("Il metodo fit e implementato ma ha sollevato un eccezzione: {}".format(e))
            
        error = []
        for i in range(len(test_data)-2):  
            valore_pred = self.predict(test_data[i:i+2])
            error.append(abs(valore_pred - test_data[i+2]))
        mae_error = sum(error)/len(error)
        return mae_error

    
    
test_data1 = [1,2,3,4,5,6,7,8,9,10.5,11.5,11.2]
trend_model = TrendModel()
evaluation_res = trend_model.evaluate(test_data1)

trend_model2 = FitTrendModel()
evaluation_res2 = trend_model2.evaluate(test_data1)

print(evaluation_res)
print(evaluation_res2)

file = CSVFile("shampoo_sales.csv")
test_data2 = file.get_data()  

trend_model3 = TrendModel()
evaluation_res3 = trend_model3.evaluate(test_data2)

trend_model4 = FitTrendModel()
evaluation_res4 = trend_model4.evaluate(test_data2)

print(evaluation_res3)
print(evaluation_res4)