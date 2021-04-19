#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    O fatorial de um número inteiro n, denotado por n!, é dado pela seguinte fórmula:
        n! = n*(n-1)*(n-2) ... 2*1
    Dessa forma, 5! = 5*4*3*2*1 = 120. Por definição, 0! = 1.
    Dado um número inteior não-negativo n, escreva uma função que calcule e devolva n! com a seguinte interface:
        def fatorial(n):
"""
# def fatorial(n):
#     soma = 1
#     numero = 1
#     if n == 0:
#         print(1)
#     else:
#         while numero <= n:
#             soma = soma * numero
#             numero = numero + 1
#         print(soma)

# n = int(input('Informe um número inteiro: '))
# fatorial(n)
# exit(0)

# codigo que o professor ajudou a fazer

def fatorial(n):
    mult = 1
    numero = 1

    while numero <=n:
        mult = mult * numero
        numero = numero + 1
    return mult

n = int(input('Informe n: ')) # variaveis são indepentendes. o n de dentro da função, é uma variavel local a função, a modificação será para esta variavel.
fat = fatorial(n)
print('Soma dos %d primeiros inteiros é %d' %(n, fat))
exit(0)

# outra forma de fazer
# aqui fará 5*4*3*2*1, mas, omitindo a ultima multiplicação, porque vezes 1, não muda muito.
"""
def fatorial(n):
    mult = 1
    while n >= 2:
        mult = mult * n
        n = n - 1
    return mult
"""