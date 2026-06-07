def elimina_duplicati(file):
    with open(file, "r") as file:
        lista_righe = []
        for line in file:
            if line not in lista_righe:
                lista_righe.append(line)
    with open("unique.txt", "a") as unique:
        for line in lista_righe:
            unique.write(line)
            print(line)


file = "hong_kong.txt"

elimina_duplicati(file)