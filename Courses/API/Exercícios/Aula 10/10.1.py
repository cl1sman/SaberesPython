n = int(input())

lista = []

while n > 0: # aqui apenas pego os valores
    lista.append(int(input()))
    n -= 1 # decremento

i = len(lista)-1 # tamanho da lista menos 1. por que?

while i >= 0: # aqui imprime a os valores invertidos. pelo que vi, não inverte a lista, apenas printa os valores invertidos.
    print(lista[i])
    i -= 1
