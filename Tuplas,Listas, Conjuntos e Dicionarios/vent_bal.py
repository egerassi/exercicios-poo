linhas, colunas, posInicial = [int(w) for w in input().split()]

while linhas != 0 and colunas != 0 and posInicial != 0:

    index = posInicial - 1

    for i in range(linhas):
        linhaCaixa = [int(w) for w in input().split()]
        deslocamento = 0

        if linhaCaixa[index] != 0:
            outcome = "BOOM "+str(index+1)+' '+str(i+1)
            break
    #loop pra achar os ventiladores mais proxims
        j = index
        while True:
            if linhaCaixa[j+1] != 0:
                ventD = j+1
                break
            else:
                j += 1
        j = index
        while True:
            if linhaCaixa[j-1] != 0:
                ventE = j-1
                break
            else:
                j -= 1
        vents = [ventE,ventD]
        ventsC = set(vents)

        deslocamento = linhaCaixa[0] - linhaCaixa[-1]
        minimo = min(deslocamento+index, index)
        maximo = max(deslocamento+index, index)
        
        desl = set(range(minimo,maximo+1))
        
        boom = True if ventsC & desl else False
        
        if boom:
            if linhaCaixa[ventE] > linhaCaixa[ventD]:
                outcome = "BOOM "+str(maximo+1)+' '+str(i+1)
            else:
                outcome = "BOOM "+str(minimo+1)+' '+str(i+1)
            break

        index += deslocamento
        outcome = "OUT "+str(index+1)

    print(outcome)
    linhas, colunas, posInicial = [int(w) for w in input().split()]