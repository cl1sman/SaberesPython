# 12.1 Diego Padilha Rubert

def linha_nula(A, i):
  for valor in A[i]:
    if valor != 0:
      return False
  return True

def coluna_nula(A, j):
  for i in range(len(A)):
    if A[i][j] != 0:
      return False
  return True

# incio implementação
m = int(input())
n = int(input())
A = []

for i in range(m):
    A.append([int(j) for j in input().split()])
# fim implementação

lnulas = 0
for i in range(m):
  if linha_nula(A, i):
    lnulas += 1
  
cnulas = 0
for i in range(n):
  if coluna_nula(A, i):
    cnulas += 1

print(f'Linhas nulas: {lnulas}')
print(f'Colunas nulas: {cnulas}')