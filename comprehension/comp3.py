def tripletta_pitagorica_check(a,b,c):
    if a**2 + b**2 == c**2:
        return True
    else:
        return False


lista_pitagorica = [(a**2 + b**2) for a in range(1,20) for b in range(1,20) for c in range(1,20) if tripletta_pitagorica_check(a,b+1,c+2)]

print(lista_pitagorica)