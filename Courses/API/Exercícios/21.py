#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Uma pessoa resolver fazer uma aplicação em uma poupança
programada. Para calcular seu rendimento, ela deverá fornecer o
valor constante da aplicação mensal, a taxa e o número de
meses. A fórmula usada para o cálculo do valor acumulado é a
seguinte:
Valor acumulado = (P*(1+i)^n -1) / i

Onde i = taxa, P = aplicação mensal e n é o número de meses.
"""

aplicação_mensal = float(input('Valor constante da aplicação mensal: R$'))
taxa = float(input('Taxa: %'))
número_de_meses = int(input('Número de meses: '))

valor_acumulado = aplicação_mensal*(1+taxa)**taxa-1 / taxa
print(f'R${valor_acumulado:.2f}')

exit(0)