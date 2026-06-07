def contatore_vendite (file):
    sum = 0
    with open(file, "r") as file_v:

        for line in file_v:
            elemento = line.strip().split(",")

            if elemento[0] != "Date":
                sum += float(elemento[1])
                print(elemento[1])
        
    return sum


file = "shampoo_sales.csv"

somma = contatore_vendite(file)

print(somma)