a= float(input())
b= float(input())
c= float(input())

isTriangle = abs(a) + abs(b) > abs(c) and abs(b) + abs(c) > abs(a) and abs(a) + abs(c) > abs(b)

print(isTriangle)