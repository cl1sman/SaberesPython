# Lari
m = int(input())
n = int(input())
matriz = []

### Armazenando os valores das listinhas na listona & formando a matriz. 
for i in range(m):
  matriz.append([int(j) for j in input().split()])

### Analisando a soma da diagonal principal.
soma_DP = 0
for i in range(m): 
  soma_DP += matriz[i][i] 

### Analisando a soma de cada linha.
linhas = []
for i in range(m): # Analisando linha a linha da matriz.
    soma_linha = 0
 
    # Analisando cada valor dentro da linha.
    for valor in matriz[i]: 
        soma_linha += valor
    linhas.append(soma_linha) # Armazenando a soma de cada linha em uma lista para possível verificação.
    
    # Verificando se as somas dos valores de cada linhas são iguais.
    for j in linhas:  
        if soma_linha != j:
            print("A matriz não é um quadrado mágico pois a soma das linhas não são iguais.")
            break

### Analisando a soma de cada coluna.
colunas = []
for i in range(n):
    soma_coluna = 0

    # Analisando cada valor dentro da coluna.
    for coluna in range(m):
        soma_coluna += matriz[coluna][i]
    colunas.append(soma_coluna)

    # Verificando se as somas dos valores de cada coluna são iguais.
    for j in colunas:
        if soma_coluna != colunas[i]:
            print("A matriz não é um quadrado mágico pois a soma das colunas não são iguais.")

### Analisando a soma da diagonal principal.
soma_DS = 0
x = len(matriz) - 1

for i in range(m): 
    soma_DS += matriz[i][x] # Enquanto o i cresce, o x decresce.
    x -= 1

### Verificando se a matriz é um quadrado mágico.
if soma_DP == soma_DS == soma_linha == soma_coluna: 
    print("A matriz é um quadrado mágico!")