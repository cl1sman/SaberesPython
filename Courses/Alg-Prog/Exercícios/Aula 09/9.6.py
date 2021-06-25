def primo(p):
    total = 0
    for contador in range(1, p + 1): # mais um, porque no for, ele não vai até o numero
        if p % contador == 0:
            total += 1
    if total == 2: # primo, divisivel por 1 e por ele mesmo, ou seja, duas vezes. então conto quantas vezes foi dividido.
        return True
    else:
        return False

n = int(input())
i = 0
soma = 0

while i < n:
    sequencia = int(input())
    if primo(sequencia) == True:
        soma += sequencia
    i += 1
print(f'soma dos números primos da sequencia: {soma}')