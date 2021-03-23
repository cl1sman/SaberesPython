#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Escreva um programa que recebe o raio de um círculo, calcula e
mostra o valor da área desse círculo.
"""

# A = pi*r^2

from math import pi

raio = float(input('Informe o raio do círculo: '))

area = pi*raio**2

print(f'Área do círculo: {area:.2f}')

exit(0)