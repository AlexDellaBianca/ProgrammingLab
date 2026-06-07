def lista_lettera(lista):
    dict = {0:"zero", 1:"uno"}
    ris = []
    for numero in lista:
        nome_new = dict[numero]
        ris.append(nome_new)
    return ris


list = [1,0,0,1,0]

riss = lista_lettera(list)

print(riss)