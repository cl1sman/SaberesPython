S = [ int(v) for v in input().split() ]

tamanho = len(S)

cont = 0
for i in range(1, tamanho - 1):
    pico = S[i]

    if S[i-1] < pico > S[i+1]:
        cont += 1

cont2 = 0
for i in range(1, tamanho - 1):
    vale = S[i]

    if S[i-1] > vale < S[i+1]:
        cont2 += 1

print (cont, cont2)