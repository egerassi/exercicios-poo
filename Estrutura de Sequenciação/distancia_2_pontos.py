from math import sqrt

x1, y1 = [float(w) for w in input().split()]

x2, y2 = [float(w) for w in input().split()]

distancia = sqrt((x1 - x2)**2+(y1 - y2)**2)

print(f"{distancia:.4f}")