# => código do Pedro Lopez[monitor]
#
# Faça um programa que, dada uma matriz de números reais Am×n, determine At
# Ou seja, imprima a matriz transposta (inversa). As linhas viram colunas e as colunas viram linhas.
#

m = int(input())
n = int(input())

mat = []
transversa = []

for i in range(m):
    mat.append([int(j) for j in input().split()]) # matriz mXn

# [[1, 2, 3],
# [4, 5, 6],
# [7, 8, 9]]

for i in range(m): # Acessa cada linha
    linha = []
    for j in range(n): # Acessa cada coluna
        linha.append(mat[j][i])
#
# Esse "mat[j][i]" com o j no primeiro colchetes, ele deixa o j fixo e muda apenas o i.
# Pegando todos os valores da primeira coluna até q a coluna acabe e pule p próxima, daí sim mudaria o i.
#
# Agora, se fosse "mat[i][j]" ele ia deixar o i fixo (coluna) e ia mudar o j, logo ele pegaria
# todos os valores da linha, sem pular pra próxima linha, ou seja, só o j mudaria até que a linha acabasse.
#
    transversa.append(linha)

print(transversa)