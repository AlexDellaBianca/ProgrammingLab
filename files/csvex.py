class CSVFILE:
    def __init__(self,file1):
        self.name = file1

        if not isinstance(self.name, str):
            raise TypeError(f"Il nome del file \"{self.name}\" non è una stringa!")
        
        try:
            file_temp = open(self.name, "r")
        except FileNotFoundError:
            print(f" \n \n Il file: {self.name} non esiste")
        else:
            file_temp.close()

    def numero_di_righe(self):
        self.num_righe = 0
        for line in self.name:
            self.num_righe += 1


    def get_data(self, start = None, end= None):

        self.start = start
        self.end = end

        check = False
        while check == False:
            numero = input(f" Dammi un numero INTERO tra 0 e {self.num_righe + 1}")
            if not isinstance(self.start, int):
                continue
            
            # Se è nell'intervallo
            if numero < 0 or numero > self.num_righe:
                check = True
            
        self.start = numero
        



        while not isinstance(self.start, int):
            self.start = input(f" Dammi un numero INTERO tra 0 e {self.num_righe + 1}")
        while self.start < 0 or self.start > self.num_righe:
            self.start = input(f" Dammi un numero tra 0 e {self.num_righe + 1}")

        while not isinstance(self.end, int):
            self.start = input(f" Dammi un numero INTERO tra 0 e {self.num_righe + 1}")
        while self.start < 0 or self.end > self.num_righe or self.end < self.start:
            self.start = input(f" Dammi un numero tra {self.start} e {self.num_righe + 1}")
    

        try:
            lista_final = []
            with open(self.name, "r") as file_in_questione:

                for line in file_in_questione:
                        lista_piccola=(line.split(","))
                        if lista_piccola[0] != "Date":
                            lista_final.append(lista_piccola)

                return lista_final
                
        except FileNotFoundError:
            print("errore file non trovato")

class NumericalCSVFile(CSVFILE):
    
    def get_data(self):
        lista_mod = super().get_data()

        try:
            for lista in lista_mod:

                for sub_list in lista_mod:
                    sub_list[1] = float(sub_list[1])
        except ValueError:
            pass


        return lista_mod




file = "shampoo_sales.csv"

filen = NumericalCSVFile(file)

lista_prova = filen.get_data()

for item in lista_prova:
    for sub in item:
        print(sub)
