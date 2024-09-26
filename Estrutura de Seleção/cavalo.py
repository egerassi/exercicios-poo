x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

canMove = False

if x1 and y1 and x2 and y2 in range(1,9):
    if (x2 == x1 -2 or x2 == x1 + 2) and (y2 == y1 - 1 or y2 == y1 + 1):
        canMove = True
    if (x2 == x1 - 1 or x2 == x1 + 1) and (y2 == y1 + 2 or y2 == y1 - 2):
        canMove = True

print(canMove)