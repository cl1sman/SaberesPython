"""
x = []
n = 10

i = 0
while i < n:
    x.append(int(input()))
    i += 1

print(x)

for valor in x:
    i = 0
    if valor <= 0:
        x[i] = 1
    i += 1
print(x)
"""

x = []
i = 0
while i < 10:
    valor = int(input())
    if valor <= 0:
        x.append(1)
    else:
        x.append(valor)
    print(f'X[{i}] = {x[i]}')
    i += 1