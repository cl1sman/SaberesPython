#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    Durante os 7 dias de uma determinada semana foram tomadas
    as temperaturas médias diárias de Campo Grande, MS.
    Determinar o número de dias dessa semana com temperaturas
    abaixo de zero. Faça ao menos uma simulação passo a passo da
    execução de sua solução.
"""
n = 7 # dias da semana
cont = 0
temperaturaabaixodezero = 0

while cont < n: # é a quantidade de vezes que eu vou contar (somar)
    temperaturamedia = float(input(f'Temperatura do {cont+1} dia: '))
    
    if temperaturamedia < 0:
        temperaturaabaixodezero += 1
    cont += 1
print('%d dia(s) com temperatura abaixo de zero em Campo Grande - MS' %temperaturaabaixodezero)


exit(0)