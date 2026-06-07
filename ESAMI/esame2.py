class CSVTimeSeriesFile:
    def __init__(self,name):
        self.name = name

#exception file non esiste
        try:
            file_prova = open(self.name, "r")
            file_prova.close()
        except:
            raise ExamException("Errore: Il file non esiste/inaccessibile")
        


    def get_data(self, city):

        lista_dati = []

        with open(self.name, "r") as File_dati:

#ciclo per line nel file
#se la città è presente nella line, svolgo un sanity check
#ovvero, faccio strip e split e vedo se il valore medio esiste ed è float.
#se è valido, lo inserisco nella lista.

#exception nome citta non in file
            city_counter = 0
            

            for line in File_dati:

                line = line.strip("\n")
                line = line.split(",")

                if city == line[2]:

                    city_counter += 1
                    
                    try:
                        line[1] = float(line[1])
                        lista_dati.append(line[0:2])

                    except ValueError:
                        pass

            
            if city_counter == 0:
                raise ExamException("Errore: città non in FILE!")
            else:
                print(f"ottenuto dati da {city_counter} istanze... \n \n")
    
        return lista_dati






class ExamException(Exception):
    pass

def media_annuale(lista):
    
    return sum(lista)/len(lista)

def media_chiavi(diz):
    
    somma_chiavi = 0
    counter = 0

    for key in diz:
        somma_chiavi += key
        counter += 1
    
    return somma_chiavi/counter

def temp_mean(diz):

    sum_temp = 0
    counter = 0

    for key in diz:
        sum_temp += diz[key]
        counter += 1

    
    return sum_temp/counter


def coeff_angolare(diz, x_tilde, y_tilde):
    
    sommatoria_1 = 0
    sommatoria_2 = 0

    for key in diz:

        sommatoria_1 += (key - x_tilde)*(diz[key] - y_tilde)
        print(sommatoria_1)

        sommatoria_2 += (key - x_tilde)**2
    
    return(sommatoria_1/sommatoria_2)


#la prima sommatoria è (chiave - x_tilde)*(media - y_tilde)
#quato è n? boh fai while.



def compute_slope(time_series, first_year, last_year):


#con questo dizionario, raccoglierò i valori per anno!

    raccolta_valori = {}

    if not isinstance(first_year,int) or not isinstance(last_year,int):
        raise ExamException("Errore: valore non valido")
    
    if first_year > last_year:
        raise ExamException("Errore: intervallo non valido")
    
    if first_year < 1849 or first_year > 2013 or last_year < 1849 or last_year > 2013:
        raise ExamException("Errore: intervallo non valido")
    
    while first_year <= last_year:

        lista_tmp = [] 

#lista temporanea dove raccolgo i valori per anno
#verranno inseriti in raccolta_dati

        for sublist in time_series:
            if str(first_year) in sublist[0]:
            
                lista_tmp.append(sublist[1])
        

#gestione caso con valori annuali < 6

        if len(lista_tmp) > 6:
            raccolta_valori[first_year] = lista_tmp
        first_year += 1
    

#calcolo la media annuale per ogni chiave

    if raccolta_valori.keys == 0:
        raise ExamException("Errore: 0 anni validi!")

    for key in raccolta_valori:
        
        raccolta_valori[key] = media_annuale(raccolta_valori[key])

#calcolo la media degli anni

    x_tilde = media_chiavi(raccolta_valori)

#calcolo la media delle medie annuali

    y_tilde = temp_mean(raccolta_valori)

    m = coeff_angolare(raccolta_valori, x_tilde, y_tilde)

    return m

prova = CSVTimeSeriesFile("GlobalLandTemperaturesByMajorCity.csv")

dati_mosca = prova.get_data("Moscow")

compute_slope(dati_mosca,1983,1986)