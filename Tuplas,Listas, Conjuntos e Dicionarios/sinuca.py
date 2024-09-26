n = int(input())

bol = [int(w) for w in input().split()]

while n != 1:
    for i in range(len(bol)-1):
        if bol[i] == bol[i+1]:
            bol[i] = -1
        else:
            bol[i] = 1
    del bol[n-1]
    n -= 1

print("branca" if bol[0] == 1 else "preta")