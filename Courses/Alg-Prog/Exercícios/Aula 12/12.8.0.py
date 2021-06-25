# @ Lari
# Dadas duas matrizes de números reais A(m×n)
# e B(n×p) calcular o produto de A por B.
#

# Recebendo as quantidades de linhas e colunas da 1ª matriz.
m = int(input())
n = int(input())

# Recebendo as quantidades de linhas e colunas da 2ª matriz.
h = int(input())
p = int(input())

# Declarando as matrizes.
matriz_A = []
matriz_B = []
matriz_AB = []

for i in range(m):
    matriz_A.append([int(j) for j in input().split()])

for i in range(h):
    matriz_B.append([int(j) for j in input().split()])

# Verificando se as colunas de A são iguais às linhas de B para possíveis multiplicações.
if n == h:
    for i in range(m):  # Analisando linha a linha da matriz A.
        soma = 0
        
        for valor in matriz_A[i]: # Analisando cada valor dentro da linha de A.
            
            for k in range(p): # Analisando coluna da matriz B.
                
                for coluna in range(1): # Analisando cada valor dentro da coluna.
                    soma += valor * (matriz_B[coluna][k])
            matriz_AB.append(soma)
