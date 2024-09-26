from collections import Counter

num_perg, qtd_freq = [int(w) for w in input().split()]

while num_perg != 0 and qtd_freq != 0:
    freq_perguntas = {}
    perguntas = input().split()
    perguntas_adicionadas = 0

    for num in perguntas:
        if num not in freq_perguntas:
            freq_perguntas[num] = 1
        else:
            freq_perguntas[num] += 1

    for v in freq_perguntas.values():
        if v >= qtd_freq:
            perguntas_adicionadas += 1

    print(perguntas_adicionadas)
    num_perg, qtd_freq = [int(w) for w in input().split()]