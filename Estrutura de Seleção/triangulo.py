a = int(input())
b = int(input())
c = int(input())

if a == b == c:
    print("equilátero")
elif a == b and a != c or b ==c and b != a or a == c and a != b:
    print("isósceles")
else:
    print("escaleno")