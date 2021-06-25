def maior_primo(n):
    resultado = 0
    for i in range(1, n+1):
        if ePrimo(i) != None:
            resultado = ePrimo(i)
        return resultado

def ePrimo(n):
    count = 0
    i = 1
    while n >= i:
        if n % i == 0:
            count += 1
        i += 1
    if count == 2:
        primo = n
        return primo
teste = maior_primo(17)
print(teste)
