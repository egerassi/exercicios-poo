frase = input() + ' '

frase_cod = ''

for i in range(len(frase)):
    if frase[i] != 'p':
        frase_cod += frase[i]
    elif frase[i-1] == 'p' and frase [i] == 'p' and frase[i+1] != 'p':
        frase_cod += frase[i]        

print(frase_cod)