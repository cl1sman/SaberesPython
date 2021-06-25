# ajuda do monitor
A = [[2, 3], [1, 0], [4, 5]]
B = [[3, 1], [2, 4]]

for i in range(m):
    for j in range(n): 
        for k in range(p):
            matriz_AB[i][j] += matriz_A[i][k]*matriz_B[k][j]
