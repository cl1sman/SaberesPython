# @ Prof. Diego

m, n, p = [int(v)  for v in input().split()]
A = []
B = []

for _ in range(m):
    A.append([int(v) for v in input().split()])
for _ in range(n):
    B.append([int(v) for v in input().split()])

C = []
for i in range(m):
    C.append([0] * p)
    for k in range(p):
        valor = 0
        for j in range(n):
            valor += A[i][j] * B[j][k]
        C[i][k] = valor
for linha in C:
    print(linha)


# teste de entrada
"""
2 4 3
1 2 3 4
5 6 7 8
1 0 0
0 1 0
0 0 1
1 1 1
"""