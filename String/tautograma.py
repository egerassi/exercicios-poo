frase = input()

while frase != '*' :
    prim_letras = [frase[0].lower()]
    eh_tautograma = 'Y'
    for i in range(len(frase)):
        if frase[i] == ' ':
            prim_letras.append(frase[i+1].lower())
    for q in range(len(prim_letras)-1):
        if prim_letras[q] != prim_letras[q+1]:
            eh_tautograma = 'N'
    print(eh_tautograma)
    frase = input()