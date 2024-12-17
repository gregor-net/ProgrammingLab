class TrendModel():
    
    def predict(self, data):
        prev_data = None
        prediction = 0
        for item in data:
            if prev_data is not None:
                prediction += item - prev_data 
            prev_data = item
        prediction /= len(data) -1
        prediction += data[-1]
        return prediction
    
    
test_data = [50,52,60]    
modello = TrendModel()
predizione = modello.predict(test_data)
print(predizione)
    