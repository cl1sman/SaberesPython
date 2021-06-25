# 3,1,3,0,1,1,1,3,1,3

# Recebe o Valor "m"
n = int(input())

matriz = []

for j in range(n):
    linha = []
    for i in range(n):
        linha.append(0)
    matriz.append(linha)

cont = 1

for i in range(n):
    matriz[0][i] = cont
    cont += 1

for i in range(1, n):
    matriz[i][n - 1] = cont
    cont += 1

cont -= 1

for i in range(n - 1, -1, -1):
    matriz[n - 1][i] = cont
    cont += 1

# 5 - 4 - 3 - 2 - 1
for i in range(n - 1, 0, -1):
    matriz[i][0] = cont
    cont += 1

# a11 a22
for i in range(1, n - 1):
    matriz[i][i] = cont
    cont += 1

# a n - 1
for i in range(1, n - 1):
    matriz[(n - 1) - i][i] = cont
    cont += 1

tam_cont = len(str(cont))

for linha in matriz:
    for item in linha:
        if len(str(item)) < tam_cont:
            print("0" * (tam_cont - 1 ) + str(item), end=" ")
        else:
            print(item, end=" ")
    print()