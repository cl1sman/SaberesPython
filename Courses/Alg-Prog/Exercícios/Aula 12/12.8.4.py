m = int(input('Numero de linhas da Matriz A = '))
n = int(input('Numero de colunas da Matriz A = '))


h = int(input('Numero de linhas da Matriz B = '))
p = int(input('Numero de colunas da Matriz B = '))


A = []
B = []
AB = []


for i in range(m):
    A.append([int(j) for j in input('Matriz A = ').split()])


for i in range(h):
    B.append([int(j) for j in input('Matriz B = ').split()])


for i in range(m):
    linha = []
    for j in range(p):
        linha.append(0)
    AB.append(linha)

for i in range(m):
    for j in range(n): 
        for k in range(p):
            (AB[i][j]) += (A[i][k]) * (B[k][j])

print(f'Matriz AB = [{AB}]')
