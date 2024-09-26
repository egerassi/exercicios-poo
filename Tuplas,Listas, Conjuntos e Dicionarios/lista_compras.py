n = int(input())

for i in range(n):
    lista = input().split()
    sem_duplicados = []

    for item in sorted(lista):
        if item not in sem_duplicados:
            sem_duplicados.append(item)
    
    output = ''

    for item in sem_duplicados:
        output += item + ' '
    print(output)