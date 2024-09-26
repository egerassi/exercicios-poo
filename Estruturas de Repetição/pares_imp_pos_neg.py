n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())
n5 = int(input())

numeros = [n1,n2,n3,n4,n5]

par = 0
impar = 0
positivo = 0
negativo = 0

for numero in numeros:
    if numero % 2 == 0:
        par += 1
    else:
        impar +=1
    if numero > 0:
        positivo += 1
    elif numero < 0:
        negativo += 1

print(f"{par} valor(es) par(es)")
print(f"{impar} valor(es) impar(es)")
print(f"{positivo} valor(es) positivo(s)")
print(f"{negativo} valor(es) negeativo(s)")