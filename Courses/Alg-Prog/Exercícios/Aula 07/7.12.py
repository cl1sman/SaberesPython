#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    Dados o número n, inteiro positivo, de estudantes de uma turma
    de Algoritmos e Programação e suas notas de primeira prova,
    determinar a maior e a menor nota obtidas por essa turma, onde
    a nota mínima é 0 e a nota máxima é 100. Faça ao menos uma
    simulação passo a passo da execução de sua solução.
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

print(f'Dia de maior venda da semana: {diademaiorvendas}° dia. Número de discos vendidos: {maior}.')


exit(0)