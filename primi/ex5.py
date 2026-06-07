

def sum_er (lista):
    s=0
    for item in lista:
        
        s = s + item
    
    return s


new_list = [1,2,3,4,5]
sum = 0

sum = sum_er(new_list)

print(sum)