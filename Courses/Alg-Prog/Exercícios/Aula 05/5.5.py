#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Dados dois números inteiros a e b, escreva “SIM” se a é ao
mesmo tempo par, positivo e múltiplo de b, OU se b é ao mesmo
tempo ímpar, múltiplo de a e diferente de a. Caso contrário,
escreva “NÃO”.
"""

a = int(input())
b = int(input())

if a % 2 == 0 and a > 0 and a % b or b % 2 and b % a and a != b:
    print('SIM')
else:
    print('NÃO')

exit(0)