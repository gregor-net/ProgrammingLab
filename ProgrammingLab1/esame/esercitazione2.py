class ExamException(Exception):
    pass

class CSVTimeSeriesFile:
    def __init__(self, name):
        self.name = name
            
    def get_data(self):
        try:
            self.file = open(self.name)
        except:
            raise ExamException('Impossibile aprire il file')
        
        l1=[]
        lista = self.file.read()
        lista = lista.split("\n")
        
        if len(lista)< 1:
            raise ExamException('Il file e vuoto')
        if len(lista) < 3:
            raise ExamException('Il file non ha valori')
        
        for item in lista:
            if item != "":
                item = item.split(",")
                if item[0] != "date":
                    l2 = []
                    l2.append(item[0])
                    try:
                        if(int(item[1]) > 0):
                            l2.append(int(item[1]))
                        else:
                            print("Non e un numero int")
                            l2.append("")
                    except:
                        print("Non e un numero int")
                        l2.append("")
                    l1.append(l2)
        return l1


def compute_variations(time_series, first_year, last_year):
    diz = {}
    year = int(first_year)
    med = 0
    count = 1
    for i in time_series:
        tmp = i[0].split('-')
        if year > int(last_year):
            return diz
        if int(tmp[0]) >= year: 
            if int(tmp[0]) == year:
                if i[1] != "":
                    med += int(i[1])
                    count += 1
            else:
                if year != int(first_year):
                    key = str(prev_year)+str(- year)
                    diz[key] = (med/count) - (prev_med/prev_count)
                prev_med = med
                med = 0
                prev_count = count
                count = 1
                prev_year = year
                year = int(tmp[0])
    return diz
    

time_series_file = CSVTimeSeriesFile('data.csv')
time_series = time_series_file.get_data()
#print(time_series)

m = compute_variations(time_series, '1952', '1956')
print(m)