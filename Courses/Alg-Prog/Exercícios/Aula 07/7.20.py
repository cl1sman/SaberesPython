#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    Dado um natural n, calcular e imprimir o valor da seguinte soma
        1/n + 2/n-1 + 3/n-2 + ... + n/1.
    
"""

n = int(input())

i = 1

if n == 0:
    print('Não existe divisão por 0')

else:
    soma = i / n

    while i < n:
        soma += (i + 1) / (n - i)
        i += 1
    
    print(soma)

exit(0)