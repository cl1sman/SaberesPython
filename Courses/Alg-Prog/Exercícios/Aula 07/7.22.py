def conta_digitos(n, d):
    conta = 0

    while (n != 0):
        resto = n % 10
        n = n // 10
        if (resto == d):
            conta += 1
    return conta

a, b = input('Digite dois inteiros: ').split()
a, b = int(a), int(b)


d = 1

permutação = True # condição para permutação

while d <= 9:
    if (conta_digitos(a, d) != conta_digitos(b, d)): # testo para ver se não é permutação. mas, não sei se a logica está, por que se os digitos estiverem em posições diferentes
        permutação = False
    d += 1

if (permutação == True):
    print(f'{a} é permutação de {b}')
else:
    print(f'{a} não é permutação de {b}')