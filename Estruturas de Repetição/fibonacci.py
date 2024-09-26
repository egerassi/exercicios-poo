n = int(input())

fibonacci = [1,1]

for i in range(3, n+1):
    fibonacci.append(fibonacci[i - 2] + fibonacci [i - 3])

print(fibonacci[n-1])