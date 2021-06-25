#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    Uma loja de discos anota diariamente durante uma determinada
    semana a quantidade de discos vendidos. Determinar em que dia
    dessa semana ocorreu a maior venda e qual foi a quantidade de
    discos vendida nesse dia. Faça ao menos uma simulação passo
    a passo da execução de sua solução
"""

n = 7 # semana
dia = 0
maior = 0

while dia < n: # é a quantidade de vezes que eu vou contar (somar)
    numerodevendas = int(input(f'Número de discos vendidos, no dia: {dia + 1}: '))
    
    if numerodevendas >= maior:
        maior = numerodevendas
        diademaiorvendas = dia + 1

    dia += 1

if diademaiorvendas == 1:
    print(f'Dia de maior venda da semana: {diademaiorvendas}° dia. Número de discos vendidos: {maior}.')


exit(0)