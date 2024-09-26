n1 = float(input()) #notas
n2 = float(input())
n3 = float(input())

p1 = int(input()) #pesos
p2 = int(input())
p3 = int(input())

media = (n1*p1 + n2*p2 + n3*p3) / (p1 + p2 + p3)

if media >= 6.0:
    print(True)
else:
    print(False)