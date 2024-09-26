L, D =[int(w) for w in input().split()]
K, P = [int(w) for w in input().split()]

custo = (L * K) + (int(L/D)*P)

print(custo)