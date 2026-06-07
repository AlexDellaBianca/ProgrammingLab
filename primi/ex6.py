array = [1,2,3,2,1]

def summer (array):
    sum = 0
    for item in array:
        sum = sum + item
    return sum

def palindrome_check (array):
    #se il numero al contrario = numero normale
    #è palindromo
    invert = array[:-1:]



y = summer(array)
x = palindrome_check(array)


print(y,x)


