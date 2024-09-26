n = 1

def fatorial(x):
    resultado = 1
    for i in range(0,x-1):
        resultado *= (x - i)
    return resultado

while True:
    if fatorial(n) > n**10:
        print(n)
        break
    else:
        n += 1