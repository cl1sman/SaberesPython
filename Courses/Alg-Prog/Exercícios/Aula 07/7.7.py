#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Dado um número inteiro positivo n e uma sequência de n inteiros
positivos, somar os números pares e os números ímpares.
    Exemplo:
        Se n = 7 e a sequência de números inteiros é 6; 1; 3; 14; 4; 22; 7
        a saída deve ser 46(= 6 + 14 + 4 + 22) e 11(= 1 + 3 + 7).
Faça ao menos uma simulação passo a passo da execução de
sua solução.
"""

n = int(input('Informe n: '))
soma_par = 0
soma_impar = 0
cont = 0

while cont < n: # é a quantidade de vezes que eu vou contar (somar)
    sequencia = int(input('Um número inteiro: '))
    
    if sequencia % 2 == 0:
        soma_par = soma_par + sequencia
    else:
        soma_impar = soma_impar + sequencia
    cont += 1
print('Da sequencia informada, a soma dos numeros pares: %d e ímpares %d' %(soma_par, soma_impar))

exit(0)