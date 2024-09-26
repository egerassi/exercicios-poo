notas = [float(w) for w in input().split()]

notas.remove(min(notas))
notas.remove(max(notas))

print(f"{sum(notas):.1f}")