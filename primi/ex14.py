import random
random = 0

#classe coin open

class Coin():
    def __init__(self, face):
        self.face = face

    def lanciare(self):

        if random.randint(0,1) == 0:
            self.face = "testa"
        else:
            self.face = "croce"

    def che_faccia(self):
        return self.faccia

#classe coin close

moneta =Coin("testa")
moneta.lanciare()
print(moneta.che_faccia)

