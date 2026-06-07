def conta_istanze(file):
    counter = 0
    with open(file, "r") as file1:
        for line in file1:
            riga = line.strip()
            counter += riga.count("hong kong")
    return counter


file = "hong_kong.txt"


i = conta_istanze(file)
print(i)