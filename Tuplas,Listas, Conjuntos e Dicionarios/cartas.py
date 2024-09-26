sequencia = [int(w) for w in input().split()]

if sequencia == sorted(sequencia):
    print("C")
elif sequencia == sorted(sequencia, reverse=True):
    print("D")
else:
    print("N")