A = [[2, 3], [1, 0], [4, 5]]
B = [[3, 1], [2, 4]]

soma = 0
for i in A:
    for j in B:
        soma += linha_nula(A,i) * coluna_nula(A,j)
