linha = int(input())
coluna = int(input())
A = []

"""
    Basicamente, o primeiro for, é apenas para criar uma lista, com posições
    que vai receber nestas, outras listas, ou seja, quantos espaços
    esta lista vai ter. E dentro destes espaços, outras listas.
    Assim, dentro destas listas, vou colocar os elementos. A primeira lista
    basicamente, é uma lista, que vai comportar outras listas.
"""
for i in range(linha): # um for mexendo na linha, e na posição de casa lista, vai se criar outra lista com outros elementos
    A.append([int(j) for j in input().split()])

# linha zero
conta_linha = 0
for i in A:
    conta = 0
    for j in i:
        if j == 0:
            conta += 1
    if conta == coluna:
        conta_linha += 1

# coluna
k = 0
lista = []
conta_coluna = 0
while k < coluna:
    
    for i in A:
        lista.append(i[k])
    
    conta = 0
    for i in lista:
        if i == 0:
            conta += 1
    if conta == linha:
        conta_coluna += 1
    lista = []
    k += 1

print(f'Colunas nulas: {conta_coluna}')
print(f'Linhas nulas: {conta_linha}')
print(A)