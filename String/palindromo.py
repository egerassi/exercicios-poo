frase = input()

frase_limpa = ''
i = 0
j = -1


for letra in frase:
    if letra.isalpha():
        frase_limpa += letra

eh_palindromo = True
for car in range(0,len(frase_limpa)-1):
    if frase_limpa[i] != frase_limpa[j]:
        eh_palindromo = False
        break
    else:
        i += 1
        j -= 1

print(eh_palindromo)
