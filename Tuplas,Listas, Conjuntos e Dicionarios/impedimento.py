atac,defe = [int(w) for w in input().split()]

while atac != 0  and defe != 0:
    pos_atac = [int(w) for w in input().split()]
    pos_def = [int(w) for w in input().split()]

    ataMaisPerto = min(pos_atac)

    impedido = "N"

    for pos in sorted(pos_def[0:2]):
        if ataMaisPerto < pos:
            impedido = "Y"
            break
    
    print(impedido)

    atac,defe = [int(w) for w in input().split()]