class Persona:
    def __init__(self, ruolo, nome, cognome):
        self.ruolo = ruolo
        self.nome = nome
        self.cognome = cognome

    def saluta(self):
        print("Ciao sono", self.ruolo + ",", self.nome, self.cognome)





class Studente(Persona):
    def __init__(self,nome,cognome,corsi):
        super().__init__("Studente UNITS", nome, cognome)
        self.corsi = corsi

    def __contains__(self, other):
        for item in self.corsi:
            if item not in other.corsi:
                return False
    
        return True
    
    def saluta(self):
        Persona.saluta(self)
        print("> frequento i corsi: ")
        print(*self.corsi, sep= "-" )
        print("\n")

class Docente(Persona):
    def __init__(self, nome, cognome, corsi):
        super().__init__("Docente UNITS", nome, cognome)
        self.corsi = corsi
    
    def saluta(self):
        Persona.saluta(self)
        print("> Docente dei corsi:")
        print(*self.corsi, sep= "-" )


corsi_franco = ["Matematica", "Machine Learning", "Padel"]
Franco = Studente("Franco", "Borro", corsi_franco)
Franco.saluta()



corsi_torro = ["Matematica", "Machine Learning", "Hockey"]
Torro = Docente("Alfredo", "Torro", corsi_torro)
Torro.saluta()

print(Torro in Franco)





