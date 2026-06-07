class CsvFile:
    def __init__(self,name_file):
        self.name_file = name_file

    def get_data(self):
        lista = []
        with open (self.name_file) as file:
            for riga in file:
                lista.append(riga.strip().split(","))
            return lista
        


file = CsvFile("shampoo_sales.csv")
print (file.get_data())


