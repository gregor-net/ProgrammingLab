class ExamException(Exception):
    pass

class MovingAverage:
    def __init__(self, window=2):
        if window < 1:
            raise ExamException('La finestra deve essere piu grande di 1')
        if not isinstance(window, int):
            window = int(window)
            print('La grandezza e definita in numeri naturali, forse intendevi {}?'.format(window))
        
        self.window = window
    
    def compute(self,data):
        
        if not isinstance(data, list):
            raise ExamException('Data non e una lista')
        if len(data) < 2:
            raise ExamException('La lista e troppo piccola')
        if len(data) < self.window:
            raise ExamException('La finestra e troppo grande')
        
        l = []
        media = 0
        for i in range(len(data) - self.window + 1):
            media = 0
            for j in range(self.window):
                media += data[i+j]
            media /= self.window
            l.append(media)
        return l
        
m = MovingAverage(5)
data1 = [2,4,8,16]
result = m.compute(data1) 
print(result)       