num_romano = input() + ' '

valores_romanos = {'M':1000, 'D':500, 'C': 100, 'L':50, 'X':10, 'V':5, 'I':1, ' ':0}

num_decimal = 0

i = 0

while i <= (len(num_romano)-2):
    if valores_romanos[num_romano[i]] >= valores_romanos[num_romano[i+1]]:
        num_decimal += valores_romanos[num_romano[i]]
        i += 1
    else:
        num_decimal += valores_romanos[num_romano[i+1]] - valores_romanos[num_romano[i]]
        i += 2

print(num_decimal)