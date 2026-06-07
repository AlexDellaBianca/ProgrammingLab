def duplicati(file):
    nuovo_file = open("unique.txt", "w")
    copia = []

    with open(file, 'r') as file:
        for row in file:
            if row in copia:
                next
            else:
                copia.append(row)

    for frase in copia:
        nuovo_file.write(frase)

    nuovo_file.close()