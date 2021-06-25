#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# funções:

# Linha
def soma_linha(A, i):
  soma = 0
  for valor in A[i]:
    soma += valor
  return soma

# Coluna
def soma_coluna(A, j):
    soma = 0
    for i in range(len(A)):
        soma += A[i][j]
    return soma

# Diagonal Principal
def soma_diagonal_principal(A, i): # A[0][0]
    soma = 0
    for i in range(len(A)):
        soma += A[i][i]
    return soma

# Diagonal Secundaria
def soma_diagonal_secundaria(A):
    soma = 0
    j = len(A) - 1
    for i in range(len(A)):
        soma += A[i][j]
        j += -1
    return soma

# input
n = int(input())
A = []

for i in range(n):
  A.append([int(j) for j in input().split()])

# SOMAS
# soma das linhas
A_soma_das_linhas = []
for i in range(n):
  A_soma_das_linhas.append(soma_linha(A, i)) # a soma de cada linha vai ser salva na lista vazia

# soma das colunas
A_soma_das_colunas = []
for i in range(n):
    A_soma_das_colunas.append(soma_coluna(A, i))

# soma da diagonal principal
A_soma_da_diagonal_principal = []
for i in range(1):
    A_soma_da_diagonal_principal.append(soma_diagonal_principal(A, i))

# soma das diagonal secundaria
A_soma_da_diagonal_secundaria = []
A_soma_da_diagonal_secundaria.append(soma_diagonal_secundaria(A))


# Comparações
x = A_soma_das_linhas[0]

verdade = True
while verdade:
    for i in A_soma_das_linhas:
        if i != x:
            verdade = False
            break
    for i in A_soma_das_colunas:
        if i != x:
            verdade = False
            break
    if x != A_soma_da_diagonal_principal[0]:
        verdade = False
        break
    if x != A_soma_da_diagonal_secundaria[0]:
        verdade = False
        break
    if verdade:
        break



print('soma das linhas', A_soma_das_linhas)
print('soma das colunas', A_soma_das_colunas)
print('soma da diagonal principal', A_soma_da_diagonal_principal)
print('soma da diagonal secundaria', A_soma_da_diagonal_secundaria)

if verdade == True:
    print('A matriz é um quadrado magico')
else:
    print('A matriz não é um quadrado magico')

exit(0)