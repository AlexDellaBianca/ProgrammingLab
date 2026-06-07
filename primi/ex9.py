def librarian (lista_parole):
    dizionario = {}
    for word in lista_parole:
        if word not in dizionario:
            dizionario[word] = 1
        
        else:
            dizionario[word] += 1
        
    return dizionario





lista_parole = ["armadio", "sedia", "copriletto", "sedia", "armadio", "armadio"]

dizio = librarian(lista_parole)

print(dizio.items())