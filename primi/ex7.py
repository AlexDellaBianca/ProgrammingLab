
def scambia (array, i, j):
    tmp = array[i]
    
    if i > 0 and j > 0 and i < len(array) and j < len(array):
        array[i], array[j] = array[j], array[i]

    else:
        print("errore!")
        return
    
    print(array)



array = [1,2,3,4,5,6]
indexes = [2,5]

scambia(array, indexes[0], indexes[1])

array.append(777)
print(array)
