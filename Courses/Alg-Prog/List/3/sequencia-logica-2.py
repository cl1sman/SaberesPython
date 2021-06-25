"""
    Escreva um programa que leia dois valores X e Y. A seguir,
    mostre uma sequência de 1 até Y, passando para a próxima linha
    a cada X números.
"""

X, Y = input().split()
X, Y = int(X), int(Y)

i = 1

while i <= Y:
    if i % X != 0: # vai printar até não ser multiplo de X. quando não for mais, ele sai deste if e retorna para o laço.
        print(i, end=' ')
    else:
        print(i)
    i += 1
exit(0)