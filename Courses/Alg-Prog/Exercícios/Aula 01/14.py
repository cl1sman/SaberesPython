#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Escreva um programa que recebe uma temperatura em graus
Fahrenheit, transforma e mostra a temperatura em graus Celsius.
"""

fahrenheit = float(input('Temperatura em Fahrenheit(F°): '))
print(f'Temperatura em Celsius(C°): {(fahrenheit-32) * 5/9:.1f}')

exit(0)