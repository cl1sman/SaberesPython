# @ Adriel

# variaveis
a = int(input("Insira o número de linhas: "))
b = int(input("Insira o número de colunas: "))

matriz = []
resp=[]

#cria a matriz
for i in range(a):
    matriz.append([int(j) for j in input().split(" ")])

# verifica a quantidade de linhas nulas
for x in range(b):
    for y in range(a):
        resp.append(matriz[y][x])
    unicos = list(set(resp))

#imprime a resposta
if (len(resp) == len(unicos)):
    print("A matriz possui numeros repetidos")
else:
    print("A matriz não possui numeros repetidos")
