#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Dado um número inteiro positivo n e uma sequência de n inteiros,
somar esses n números.
    Exemplo:
        Para n = 5 e a sequência 5; -3; 6; 0; 12 a saída deve ser
        20(= 5 + (-3) + 6 + 0 + 12).
Faça ao menos uma simulação passo a passo da execução de
sua solução.
"""

n = int(input('Informe n: ')) # variaveis são indepentendes. o n de dentro da função, é uma variavel local a função, a modificação será para esta variavel.
soma = 0
cont = 0

while cont < n: # é a quantidade de vezes que eu vou contar (somar)
    sequencia = int(input('Informe um digito da sequencia a ser somada: '))
    soma = soma + sequencia
    cont += 1
print('A soma da sequencia de %d digitos informados é %d' %(n, soma))

exit(0)