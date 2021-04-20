#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    Dado um número inteiro positivo n e uma sequência de n números
    inteiros positivos, determinar quantos números da sequência são
    pares e quantos são ímpares.
        Exemplo:
            Se n = 6 e a sequência de números inteiros é 28; 5; 4; 9; 720; 566
            a saída deve ser 4 e 2.
    Faça ao menos uma simulação passo a passo da execução de
    sua solução.
"""

n = int(input('Número inteiro positivo: '))
cont = 0
par = 0
impar = 0

while cont < n: # é a quantidade de vezes que eu vou contar (somar)
    sequenciadenumerosinteiros = int(input('Sequência de número(s) inteiros: '))
    
    if sequenciadenumerosinteiros % 2 == 0:
        par += 1
    else:
        impar += 1
    cont += 1
print(f'Par: {par} impar: {impar}')


exit(0)