cobol = ['c','o','b','o','l']

while True:
    try:
        frase = input().split('-')
        i = 0
        bug = False
        for palavra in frase:
            if palavra[0] != cobol[i] and palavra[-1] != cobol[i]:
                bug = True
                break
            else:
                i += 1
        print("GRACE HOPPER" if bug == False else "BUG")
    except EOFError:
        break