n = int(input())
A = []
aux = 1

for i in range(n):
    A.append([])
    for j in range(n):
        A[i].append(0)


for i in range(0, n):
    A[0][i] = aux
    aux += 1

for i in range(1, n):
    A[i][n-1] = aux
    aux += 1

for i in range(n-2, -1, -1):
    A[n-1][i] = aux
    aux += 1

for i in range(n-2, 0, -1):
    A[i][0] = aux
    aux += 1

for i in range(1, n-1):
    A[i][i] = aux
    aux += 1

for i in range(1, n-1):
    A[(n-1)-i][i] = aux
    aux += 1

for i in range(n):
    for j in range(n-1):
        if A[i][j] < 10:
            print("0%i" % A[i][j], end=" ")
        else:
            print("%i" % A[i][j], end=" ")
    if A[i][n-1] < 10:
        print("0%i" % A[i][n-1], end="")
    else:
        print("%i" % A[i][n-1], end="")
    if i != n-1:
        print("")

exit(0)