val = list(map(int, input().split())) # Solicitando varios valores numa mesma linha e armazenando em lista.

N = val[1] # Armazenando o valor da posição 1 em N.
i = 1

while i < len(val): # Analisando se i é <= ao comprimento de val.
    if val[i] <= 0:
        i += 1
    else:
        break

soma = 0
for _ in range (0, val[i]):
    soma += val[0] + _ # Somando os valores (não nulos e positivos) + o valor armazenado na posição 0.

print (soma)
exit(0)