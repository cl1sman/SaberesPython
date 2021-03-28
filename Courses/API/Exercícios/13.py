#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Escreva um programa que recebe uma temperatura em graus
Celsius, transforma e mostra a temperatura em graus Fahrenheit.
"""

celsius = float(input('Temperatura em Celsius(C°): '))
print(f'Temperatura em Fahrenheit(F°): {(celsius*9/5) + 32}')

exit(0)