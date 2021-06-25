# Recebendo as quantidades de linhas e colunas da 1ª matriz.
m = int(input('Numero de linhas da Matriz A = '))
n = int(input('Numero de colunas da Matriz A = '))

# Recebendo as quantidades de linhas e colunas da 2ª matriz.
h = int(input('Numero de linhas da Matriz B = '))
p = int(input('Numero de colunas da Matriz B = '))

# Declarando as matrizes.
A = []
B = []
AB = []

# Montando a matriz A.
for i in range(m):
    A.append([int(j) for j in input('Matriz A = ').split()])

# Montando a matriz B.
for i in range(h):
    B.append([int(j) for j in input('Matriz B = ').split()])

# Armazenando 0 em todas as posições da matriz AB para que seja possível armazenar as somas posteriormente.
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
