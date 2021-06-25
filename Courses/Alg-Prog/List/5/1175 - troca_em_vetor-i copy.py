vetor = []
n = 4
# Armazenando os valores na lista.
i = 0
while i < n:
    valor = int(input())
    vetor.append(valor)
    i += 1

# Armazenando os valores em ordem inversa.
i = -1
inverso = []
while i >= -(n):
    inverso.append(vetor[i])
    i -= 1

# Imprimindo os valores em ordem inversa com a posição inicial 0.
for i in range(n):
    print("N[%d] = %d" % (i, inverso[i]))