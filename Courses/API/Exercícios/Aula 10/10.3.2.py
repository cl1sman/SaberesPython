# resolução do professor

gabarito = input().split()
n = int(input())

for _ in range(n):
    prova = input().split()
    acertos = 0

    for i in range(len(gabarito)):
        if prova[i] == gabarito[i]:
            acertos += 1
    print(acertos)