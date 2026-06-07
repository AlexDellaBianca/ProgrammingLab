
listaA = [[1,2,3],[4,5],[6,7,8,1]]

listaF = [j for sublist in listaA for j in sublist if j%2 ==0]

print(listaF)

lista_a = [1,3,5,7]
lista_b = [2,4,6]

lista_c = [(x*y) for x in lista_a for y in lista_b if x*y > 10]

print(lista_c)