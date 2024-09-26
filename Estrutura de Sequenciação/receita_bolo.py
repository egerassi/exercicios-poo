A, B, C = [int(w) for w in input().split()]

farinha = int(A / 2)

ovo = int(B / 3)

leite = int(C / 5)

bolo = min(farinha,ovo,leite)

print(bolo)