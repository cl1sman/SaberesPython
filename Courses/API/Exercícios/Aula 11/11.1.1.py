# resolução do professor

def subconjunto(A, B):
    sub = True
    for valor in A:
        if valor not in B: # ou: if not valor in B:
            sub = False
    return sub

A = [int(v) for v in input().split()]
B = [int(v) for v in input().split()]

if subconjunto(A, B) == True and subconjunto(B, A) == True:
    print('conjuntos iguais')
else:
    print('conjuntos não iguais')