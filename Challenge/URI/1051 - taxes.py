#!/usr/bin/env python3
# -*- coding: utf-8 -*-

salario = float(input())

if salario >= 0.00 and salario <= 2000.00:
    taxafinal = 0
    print('Isento')

elif 2000.00 < salario <= 3000.00:
    taxafinal = (salario - 2000) * (8/100)

elif 3000.0 < salario <= 4500.00:
    taxa8 = 1000.0 * (8/100)
    taxafinal = taxa8 + ((salario - 3000.0) * (18/100))

elif salario > 4500.00:
    taxa8 = 1000.0 * (8/100)
    taxa18 = 1500 * (18/100)
    taxafinal = ((salario - 4500) * (28/100)) + taxa8 + taxa18

# aqui faz o print
if salario > 2000.00:
    taxafinal = float(taxafinal)
    print(f'R$ {taxafinal:.2f}')

exit(0)