class CSVTimeSeriesFile:
    def __init__(self,name):
        self.name = name
    
    def get_data(self):
        with open(self.name,"r") as file_dati:

            #apertura file in READ

            lista_dati = []

#prende una lista vuota e riempie con le liste
#che ottengo dalla funzione split.

            for line in file_dati:
                if "dt,LandAverageTemperature" in line:
                    pass
                #NON inserisco l'header nella lista
                else:
                    riga_buona = line.strip("\n")

                    #rimuovo gli \n alla fine dei numeri

                    riga_buona = riga_buona.split(",")

                    riga_buona = int(riga_buona)

                    lista_dati.append(riga_buona)


            print(lista_dati)
            return(lista_dati)




