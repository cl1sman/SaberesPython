# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Dados números reais a; b e c, calcular as raízes de uma equação
do 2o grau da forma ax2 + bx + c = 0. Imprimir a solução em uma
das seguintes formas: (a) ÚNICA e o valor da raiz; (b) REAIS
DISTINTAS e os valores das duas raízes; ou (c) COMPLEXAS.
"""
import math

a = float(input('A = '))
b = float(input('B = '))
c = float(input('C = '))

delta = b**2 - 4*a*c # calculo de Delta


# print(delta, x1, x2)
if delta == 0: # caso a
    x = -b / (2*a) # tem que especificar, usando parenteses, porque senão ele fará a divisão primeiro, depois ira multiplicar
    print('a) ÚNICA', x)

elif delta > 0: # caso b
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    print('b) REAIS DISTINTAS', x1, x2)

else: # caso c
    print('c) COMPLEXAS')

exit(0)