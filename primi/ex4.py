
n = 1

def request (n):
    n = int(input("Scrivi un numero, 0 per fermarsi"))
    k=0
    while(n !=0):
        k += n
        n = int(input("Scrivi un numero, 0 per fermarsi"))

    print(k)
    return k

x = request(n)

###facciamo il fattoriale del risultato

def fattoriale(x):
    ""
    #vuol dire fare n*(n-1) FINCHE' n == 1
    ""
    y = x
    fatt = x
    while(y > 1):
        y -= 1
        fatt = fatt*y
    
    return fatt

tmp = fattoriale(x)
print(tmp)

