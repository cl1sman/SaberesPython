#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    Dado um número inteiro positivo n, imprimir os n primeiros naturais ímpares.
    exemplo:
        para n = 4 a saída deverá ser 1, 3, 5, 7.
    Faça ao menos uma simulação passo a passo da execução de sua solução.
"""
n = int(input('Informa n: '))
soma = 0
numero = 1
while soma < n:
    print(numero)
    soma = soma + 1
    numero = numero + 2
# print('Soma dos %d primerios inteiros é %d' % (n, soma))

# OUTRA FORMA DE FAZER
# n = int(input())
# cont = 1
# numero = 1
# while cont <= n: # pensar a condição, e o que vou colcar dentro. então, para saber o quando vou parar, tenho que saber o que esta dentro
#                  # em outro momento cont = 0 e cont < n
#     print(numero)
#     numero += 2 # para o proximo ímpar
#     cont += 1 # já que estou usadno o contador para contar, usarei como condição de parada

# # Outra solução, eliminando o contador. fazendo uma conta, em que o número não pode passar.
# n = int(input())
# cont = 1
# numero = 1

# while numero < 2*n:
#     print(numero)
#     numero += 2

# # Outra solução
# n = int(input())
# cont = 1

# while cont <= n:
#     print(2*cont - 1)
#     cont += 1

# # Outra solução
# n = int(input())
# cont = 0
# while cont < n:
#     print(2*cont + 1)
#     cont += 1

exit(0)