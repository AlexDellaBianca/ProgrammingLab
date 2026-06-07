
minuti = 538

def orologio(minuti):

    
    H = minuti//60
    H =int(H)

    min = minuti - (H*60)

    print(f"ORA == {H}h:{min}min") 


orologio(538)

print("///////secondo es \n \n")

lettera = "a"

parola = input("dammi una parola")

def contalettere(lettera,parola):
    """
    conta
    """
    lettera = lettera.lower()
    parola = parola.lower()
    
    k = 0
    for item in parola:
        if(item == lettera):
            k = k + 1
    
    for idx, item in enumerate(parola):
        print(idx, item)
    return k
#con enumerate stampa l'indice

ris = contalettere(lettera,parola)

print(ris)



