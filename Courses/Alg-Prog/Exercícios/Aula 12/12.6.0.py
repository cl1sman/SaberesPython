# A = [[1, 2], [3, 4], [5, 6]]

A = []

m, n = [int(v) for v in input().split()]

for _ in range(m):
    A.append([int(v) for v in input().split()])

At = []

for coluna in range(n):
    for linha in range(m):
        At.append(A[linha][coluna])

AB = []        
for i in range(m):
    AB.append(At[0])
    At.remove(At[0])

Matriz_transposta = [AB, At]
print(Matriz_transposta)