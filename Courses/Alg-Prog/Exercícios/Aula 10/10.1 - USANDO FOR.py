"""
    Imprimindo a sequencia inversa

    USANDO FOR
"""

n = int(input())
lista = []

for _ in range(n):
    lista.append(int(input())) # uso _, para não confundir. como esta variavel vai ser apenas usada para este momento, e depois destruida.

for i in range(len(lista)-1, -1, -1): # [inicio, fim [
    print(lista[i])
