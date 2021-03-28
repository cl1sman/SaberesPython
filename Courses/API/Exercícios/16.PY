#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Tendo como dado de entrada a altura (h) de uma pessoa, escreva
um programa que mostre o peso recomendado para essa pessoa
utilizando as seguintes fórmulas:
    Homens: (72.7*h) - 58
    Mulheres: (62.1*h) - 44.7
"""
h = float(input('Altura: '))

print('Peso recomendado:')
print(f'Homens: {(72.7*h) - 58:.1f}')
print(f'Mulheres: {(62.1*h) - 44.7:.1f}')

exit(0)