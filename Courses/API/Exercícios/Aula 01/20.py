#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
(Extensão do exercício 19) Faça um programa para uma loja de
tintas. O programa deverá pedir o tamanho em metros quadrados
da área a ser pintada. Considere que a cobertura da tinta é de 1
litro para cada 3 metros quadrados e que a tinta é vendida em
latas de 18 litros (que custam R$ 80,00) ou em galões de 3,6 litros
(que custam R$ 25,00). Informe ao usuário as quantidades de
tinta a serem compradas e os respectivos preços em 3 situações:
    * Comprar apenas latas de 18 litros;
    * Comprar apenas galões ed 3,6 litros;
    * Misturar latas e galões, de forma que o preço seja o menor.
    * Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
"""

# Resolution
# m^2 = 180
# e = m^2 / 3 = 60
# la (Teto) = [e / 18] = 4

# from math import ceil (teto)

from math import ceil, floor

m = int(input())
li = m / 3

print('Preço em latas: R$ {(ceil(li/18) * 80)}')
print('Preço em galões: R$ {(ceil(li / 3.6) * 25)')


# 3 galões = 10.8 litros = R$ 75 ---- compensa usar galões ----
# 4 galões = 14.4 litros = R$ 100 ---- não compensa galões, usar latas ----
li = li * 1.1 # adicionei folga, mesmo que li = li + li * 0.1
lm = floor(li / 18)
resto = li - lm * 18 # 66 - 54 = 12 / 10.8 = 1 * 80
lm = lm + floor(resto/10.8)*80