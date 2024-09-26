num_aerop, num_voos = [int(w) for w in input().split()]
teste = 1

while num_aerop != 0 and num_voos != 0:
    contagem = {value:0 for value in range(1, num_aerop+1)}

    for i in range(num_voos):
        aero1, aero2 = [int(w) for w in input().split()]
        contagem[aero1] += 1
        contagem[aero2] += 1

    valor_procurado = max(contagem.values())
    aeroporto_imprimido = ''

    for k,v in contagem.items():
        if v == valor_procurado:
            aeroporto_imprimido += str(k) + ' '

    print(f"Teste {teste}\n{aeroporto_imprimido}\n")

    teste += 1
    num_aerop, num_voos = [int(w) for w in input().split()]