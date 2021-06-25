#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Dado um número inteiro n, escreva “SIM” se ele é ao mesmo
tempo ímpar, múltiplo de 3 e múltiplo de 7. Caso contrário,
escreva “NÃO”.

Obs.: 
    * ímpar -> n % 2
    * múltiplo de 3 -> n % 3
    * múltiplo de 7 -> n % 7

link: https://www.pythonprogressivo.net/2018/03/Saber-Numero-Par-Impar-Python.html
"""

n = int(input())
if n % 2 and n % 3 and n % 7:
    print('SIM')
else:
    print('NÃO')

exit(0)