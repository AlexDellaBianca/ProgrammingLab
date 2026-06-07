class Veicolo:
    def __init__(self, anno, modello, marca):
        self.anno = anno
        self.modello = modello
        self.marca = marca
        self.speed = 0

    def __str__(self):
        #2 linee di codice per il print che se no veniva una linea di 150 colonne.

        stringa = "Macchina -> Marca: {}, Modello: {}, Anno: {}" 
        return stringa .format(self.marca, self.modello, self.anno)
    
    def accellerare(self):
        self.speed += 5
    
    def frenare(self):
        self.speed -= 5
    
    def get_speed(self):
        print(self.speed)


class Auto(Veicolo):
    def __init__(self, anno, modello, marca, porte):
        super().__init__(anno, modello, marca)
        self.numero_porte = porte

    def __str__(self):
        return super().__str__() + "; Numero porte: " + str(self.numero_porte) 

class Moto(Veicolo):
    def __init__(self, anno, modello, marca, tipo):
        super().__init__(anno, modello, marca)

        self.tipo = tipo
    
    

car = Auto(1999, "lancer","mitsubishi",4)

print(car)





#slide 26
#slide copying
