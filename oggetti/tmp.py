
def contiene(lista_a, lista_b):
    for item in lista_a:
        if item not in lista_b:
            return False
    
    return True



a = ["Matematica", "Machine Learning", "Padel"]

b = ["Matematica", "Machine Learning", "Padel"]




print(contiene(a,b))