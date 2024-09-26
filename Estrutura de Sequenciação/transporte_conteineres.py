A, B, C = [int(w) for w in input().split()]
X, Y, Z = [int(w) for w in input().split()]

maximo_conteineres = int(X/A) * int(Y/B) * int(Z/C)

print(maximo_conteineres)