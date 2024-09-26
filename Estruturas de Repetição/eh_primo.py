from math import sqrt

##n = int(input())

def verificaPrimo(n):
    eh_primo = True
    if n == 1:
        eh_primo = False
    else:
        for i in range(2, int(sqrt(n))+1):
            if n % i == 0:
                eh_primo = False
    return eh_primo


##print(verificaPrimo(n))