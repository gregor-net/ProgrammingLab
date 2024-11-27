class Veicolo():
    
    def __init__(self, modello, marca, anno):
        self.modello = modello
        self.marca = marca
        self.anno = anno
        self.speed = 0
        
    def __str__(self):
        return 'Person "{} {} {} {}"'.format(self.modello, self.marca, self.anno, self.speed)
    
    

