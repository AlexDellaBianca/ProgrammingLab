lista_int = [i for i in range(0,11)]

lista_let = ["a", "b", "c", "d", "e"]

lista_final =[(a,b) for a in lista_int for i,b in enumerate(lista_let) if a%2 == 0 and i%2 == 1]

print(lista_final)
