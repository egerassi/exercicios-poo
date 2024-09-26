x = int(input())
inicio = int(input())
final = int(input())

inInterval = False

if x in range(inicio, final + 1):
    inInterval = True

print(inInterval)