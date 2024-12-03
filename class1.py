class Veicolo():
    
    def __init__(self, modello, marca, anno):
        self.modello = modello
        self.marca = marca
        self.anno = anno
        self.speed = 0
        
    def __str__(self):
        return 'Veicolo: "{} {} {} {}"\n'.format(self.modello, self.marca, self.anno, self.speed)
    
    def accellerare(self):
        self.speed += 5
        
    def frenare(self):
        self.speed -= 5
    
    def get_speed(self):
        return self.speed

class Auto(Veicolo):
    
    def __init__(self, modello, marca, anno, numero_porte):
        super().__init__(modello, marca, anno)
        self.numero_porte = numero_porte
    
    def __str__(self):
        return 'Auto: "{} {} {} {}" \nNmero porte: "{}"\n'.format(self.modello, self.marca, self.anno, self.speed, self.numero_porte)
    
class Moto(Veicolo):
    
    def __init__(self, modello, marca, anno, tipo):
        super().__init__(modello, marca, anno)
        self.tipo = tipo
    
    def __str__(self):
        return 'Moto: "{} {} {} {}" \nTipo di moto: "{}"\n'.format(self.modello, self.marca, self.anno, self.speed, self.tipo)
 

veicolo = Veicolo("PANDA", "Fiat", "2020")

print(veicolo)
veicolo.accellerare()
veicolo.accellerare()
veicolo.accellerare()
print(veicolo.get_speed())
veicolo.frenare()
veicolo.frenare()
print(veicolo.get_speed())

auto = Auto("Polo", "VW", "2023","5")
print(auto)

moto = Moto("R1","Yamaha","2017","Sportiva")
print(moto)

        
    
    

