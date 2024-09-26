n = int(input())

for d in range(n):
    soluciona = True
    matrizsudoku = [[int(w) for w in input().split()] for i in range(9)]

    #Verifica linhas
    for k in range(9):
        valores = []
        if soluciona == False:
            break
        else:
            for num in matrizsudoku[k]:
                if num in valores:
                    soluciona = False
                    break
                else:
                    valores.append(num)

    #Verifica colunas
    for c in range(9):
        valores = []
        if soluciona == False:
            break
        else:
            for l in range(9):
                if matrizsudoku[l][c] in valores:
                    soluciona = False
                    break
                else:
                    valores.append(matrizsudoku[l][c])

    #Verifica 3x3
    valores = []
    for i in range(3):
        if soluciona == False:
            break
        else:
            for valor in matrizsudoku[i][0:3]:
                if valor in valores:
                    soluciona = False
                    break
                else:
                    valores.append(valor)

    valores = []
    for i in range(3,6):
        if soluciona == False:
            break
        else:
            for valor in matrizsudoku[i][0:3]:
                if valor in valores:
                    soluciona = False
                    break
                else:
                    valores.append(valor)

    valores = []
    for i in range(6,9):
        if soluciona == False:
            break
        else:
            for valor in matrizsudoku[i][0:3]:
                if valor in valores:
                    soluciona = False
                    break
                else:
                    valores.append(valor)

    valores = []
    for i in range(3):
        if soluciona == False:
            break
        else:
            for valor in matrizsudoku[i][3:6]:
                if valor in valores:
                    soluciona = False
                    break
                else:
                    valores.append(valor)

    valores = []
    for i in range(3,6):
        if soluciona == False:
            break
        else:
            for valor in matrizsudoku[i][3:6]:
                if valor in valores:
                    soluciona = False
                    break
                else:
                    valores.append(valor)

    valores = []
    for i in range(6,9):
        if soluciona == False:
            break
        else:
            for valor in matrizsudoku[i][3:6]:
                if valor in valores:
                    soluciona = False
                    break
                else:
                    valores.append(valor)

    valores = []
    for i in range(3):
        if soluciona == False:
            break
        else:
            for valor in matrizsudoku[i][6:9]:
                if valor in valores:
                    soluciona = False
                    break
                else:
                    valores.append(valor)

    valores = []
    for i in range(3,6):
        if soluciona == False:
            break
        else:
            for valor in matrizsudoku[i][6:9]:
                if valor in valores:
                    soluciona = False
                    break
                else:
                    valores.append(valor)

    valores = []
    for i in range(6,9):
        if soluciona == False:
            break
        else:
            for valor in matrizsudoku[i][6:9]:
                if valor in valores:
                    soluciona = False
                    break
                else:
                    valores.append(valor)

    print(f"Instancia {d+1}")
    print("SIM\n" if soluciona == True else "NAO\n")