class ExamException:
    pass


class CSVTimeSeriesFile:

    def __init__(self,name):
        
        self.name = name

#Eccezione Esistenza File

        try:
            with open(self.name, "r"):
                pass
        except FileNotFoundError:
            raise ExamException("Errore: impossibile aprire il file")
        


    def get_data(self):

        lista_dati = []
        
        with open(self.name, "r") as file_dati:

            for line in file_dati:
                if "dt,LandAverageTemperature,LandAverageTemperatureUncertainty" not in line:
                    
                    line = line.strip("\n")
                    line = line.split(",")
                    
                    #converto i valori numerici nel tipo float:
                    #(gestisco il caso dato mancante)

                    for i in [1,2]:

                        if line[i] == "":

                            line[i] = -9999.00
                            

                        else:

                            line[i] = float(line[i])

                    if line[2] > 5 or line[2] == -9999.00:
                        print("Data saltata perche valore troppo incerto")

                    if line[2] < 5 and line[2] != -9999.00:
                        lista_dati.append(line)
        return lista_dati

def compute_month_variation(time_series, first_year, second_year):

    diz_dati = {}
    lista_anno1 = []
    lista_anno2 = []
    for sublist in time_series:

            if str(first_year) in sublist[0]:
                
                for sublist2 in time_series:
                    if str(second_year) in sublist2[0]:

                        if sublist[0][3:5] == sublist2[0][3:5]:
                            
                            lista_anno1.append(sublist)
                            lista_anno2.append(sublist2)
                        else:
                            print(f"La variazione per il mese {sublist[0][3:5]} non puo essere calcolata")

    diz_dati[first_year] = lista_anno1
    diz_dati[second_year] = lista_anno2
    
    print(diz_dati)





time_series_file = CSVTimeSeriesFile("Temperatures.csv")

dati = time_series_file.get_data()


compute_month_variation(dati,1990,1995)



#--

#First year < Second year
#Solleva eccezione "Errore: gli anni inseriti devono essere di tipo intero."
#Se il secondo anno `e minore o uguale al primo
#sollevare un eccezione: "Errore: il secondo anno deve essere maggiore del primo."

#Se un mese non e presente in uno o entrambi gli anni, stampo a schermo: "La
#variazione per il mese X non pu`o essere calcolata". X sar`a il valore del mese non
#presente.

#(2 punti) Se nessun mese `e disponibile, alzare un eccezione: "Gli anni considerati non
#hanno mesi validi"
