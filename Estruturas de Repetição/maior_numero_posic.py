q = int(input())

max_num = int(input())
posicao_max_num = 1
posicao_atual = 1

for i in range(q-1):
    posicao_atual += 1
    num_atual = int(input())
    if num_atual > max_num:
        max_num = num_atual
        posicao_max_num = posicao_atual

print(f"{max_num} {posicao_max_num}")