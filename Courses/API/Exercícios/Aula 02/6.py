"""
Escreva um programa que receba um número inteiro a e verifique se a é positivo, se
a é negativo ou se a é igual a 0. Faça a simulação passo a passo da execução de
sua solução.
"""
a = int(input())

if a < 0:
    print('positivo')

elif a > 0:
    print('negativo')
else: # se não é maior, menor, é igual a zero
    print('igual a zero')