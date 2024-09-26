i1 = int(input())
i2 = int(input())

count = 0

if i2 > i1:
    for i in range(i1, i2 + 1):
            count += 1
if i1 > i2:
    for i in range(i2, i1 + 1):
            count += 1

print(count)