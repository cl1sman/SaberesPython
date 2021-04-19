#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    Dado um número inteiro positivo n e uma sequência de n números
    inteiros, determinar quantos números da sequência são positivos
    e quantos são não-positivos. Um número é não-positivo se é
    negativo ou se é igual a 0 (zero).
        Exemplo:
            Se n = 6 
            e a sequência de números inteiros é 6;-1; 0; 16;-5; 0
            a saída deve ser 2 e 4.
Faça ao menos uma simulação passo a passo da execução de
sua solução.
"""

n = int(input('Número inteiro positivo: '))
cont = 0
positivo = 0
nãopositivo = 0

while cont < n: # é a quantidade de vezes que eu vou contar (somar)
    sequenciadenumerosinteiros = int(input('Sequência de número(s) inteiros: '))
    
    if sequenciadenumerosinteiros > 0:
        positivo += 1
    else:
        nãopositivo += 1
    cont += 1
print(f'Não-positivo: {nãopositivo}; Positivo: {positivo}')

exit(0)