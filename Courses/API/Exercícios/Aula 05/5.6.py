#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Dados dois números inteiros a e b, escreva “SIM” se a é ao
mesmo tempo ímpar, não positivo, e menor que b, OU se a é
menor que -3, OU se o dobro de a é múltiplo de b, OU se b é ao
mesmo tempo ímpar, múltiplo de a e diferente de a, OU se a
diferença entre ambos é maior que 10. Caso contrário, escreva
“NÃO”.
"""

a = int(input())
b = int(input())

if a % 2 and a < 0 and a < b or a < -3 or 2*a % b or b % 2 and b % a and a != a or a-b > 10:
    print('SIM')

else:
    print('NÃO')

exit(0)