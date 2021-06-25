#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Escreva um programa que pergunte quanto você ganha por hora
e o número de horas trabalhadas por mês. Seu programa deve
calcular e mostrar o total do seu salário no referido mês.
"""

ganho_por_hora = float(input('Valor da hora R$: '))
número_de_horas_trabalhadas_mês = float(input('Número de horas trabalhadas por mês: '))

print(f'Salario total: R${ganho_por_hora * número_de_horas_trabalhadas_mês:.2f}')

exit(0)