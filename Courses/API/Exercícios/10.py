#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Escreva um programa que leia três números inteiros e mostre
como resultado a soma desses três números e também a
multiplicação desses três números. Faça a simulação passo a
passo da execução do programa.
"""

numero1 = int(input('Informe a 1° número: '))
numero2 = int(input('Informe o 2º número: '))
numero3 = int(input('Informe o 3º número: '))

soma = numero1 + numero2 + numero3
multiplicação = numero1 * numero2 * numero3

print(f'A soma dos números {numero1}, {numero2}, e {numero3} é igual a {soma}')
print(f'A multiplicação dos números {numero1}, {numero2}, e {numero3} é igual a {multiplicação}')

exit(0)