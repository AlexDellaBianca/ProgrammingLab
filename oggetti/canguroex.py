
class Canguro:
    def __init__ (self, contenuto_tasca = []):
        self.contenuto_tasca = contenuto_tasca
    
    def intasca (self, obj):
        self.contenuto_tasca.append(obj)
    
    def __str__(self):
        return f"Canguro, Contenuto tasca = {self.contenuto_tasca}"

Can = Canguro()
Guro = Canguro()

Can.intasca(45)



print(Guro)

