
def conta_parole (my_file, word):
    file_func = open(my_file, "r")
    
    counter = 0
    for line in file_func:
        if word in line:
            counter = counter + 1
    
    file_func.close()
    return counter

file = "esercizio1.txt"
parola = "love"

ris = conta_parole(file, parola)

print(ris)

