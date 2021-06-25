#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Dado um número inteiro n, escreva “SIM” se ele é ao mesmo
tempo ímpar e positivo, OU ao mesmo tempo par e negativo.
Caso contrário, escreva “NÃO”.
"""

n = int(input())

if n % 2 and n > 0 or n % 2 == 0 and n < 0:
    print('SIM')
else:
    print('NÃO')

exit(0)