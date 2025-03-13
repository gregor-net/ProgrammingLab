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
        if len(data)<=2:
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
    
class FitTrendModel(TrendModel):
       
    def fit(self, data):
        self.historical_avg_variation  = super().avg_variation(data)
    
    def predict(self, data):
        prediction = data[-1] + (self.avg_variation(data) + self.historical_avg_variation) / 2
        return prediction

    
    
test_data = [50,52,60]   
test_data2 = [8, 19, 31, 41] 
modello = TrendModel()
modello2 = FitTrendModel()
predizione = modello.predict(test_data)
print(predizione)
modello2.fit(test_data2)
predizione2 = modello2.predict(test_data)
print(predizione2)
    