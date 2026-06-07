class Persona:
    '''SUPER CLASSE'''
    def __init__(self, nome,cognome,ruolo):
        
        self.name = nome
        self.surname = cognome
        self.role = ruolo
    
    def saluta(self):
        print (f"Ciao! Sono: {self.name} {self.surname}.")
        print (f"{self.role} all'UNITS! \n")

    @classmethod
    def appartiene_UNI(cls,individuo):
        if isinstance(individuo,Persona):
            return True
        
    def __add__(self, other):
        return "huh?"

class Studente(Persona):
    def __init__(self, nome, cognome, corso):
        super().__init__(nome, cognome, "Studente UNITS")
        self.course = corso
    
    def saluta(self):
        Persona.saluta(self)
        print("frequento il corso: ", self.course)




studente1 = Persona("Marius","Bogdan","Studente")
studente1.saluta()


studente2 = Studente("Marius", "Ionascu", "AI")
studente2.saluta()

amico = "mamo"


print(studente1+studente2)
