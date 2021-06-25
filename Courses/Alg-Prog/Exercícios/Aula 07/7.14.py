"""
    Dado um número inteiro positivo n e uma sequência de n números
    inteiros, verificar se a sequência está em ordem crescente.
        Exemplo:
        Se n = 6 e a sequência é 1; 5; 9; 12; 13; 26, dizemos que a
        sequência está em ordem crescente.
"""

# ainda não sei qual é o exercício

cres = True # crescente
# como o primeiro numero lido não tem antetior, deixo ele fora.
n = (int(input())) - 1 # porque já li um antes do laço
atual = int(input())

while n > 0:
    ant = atual
    atual = int(input(n))

    if atual <= ant:
        cres = False
    n -= 1

if cres: # cres é True
    print('É crescente')
else:
    print('Não é crescente')

# o cres, é uma variavel de indicação de passagem