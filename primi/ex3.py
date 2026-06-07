n = input("dammi un numero")
n = int(n)

def is_prime(numero_in_input):
    prime = 1
    k = numero_in_input
    while(prime == 1):
        k -= 1
        
        if k==0:
            return prime
        
        if(k==1):

            return prime
        
        if(numero_in_input % k == 0):
            prime = 0

    return prime
        
if is_prime(n):
    print("primo!")

else:
    print("non primo")

