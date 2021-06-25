#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    Dado um número inteiro positivo n e uma sequência de n números
    inteiros, determinar a soma dos números inteiros positivos da
    sequência.
        Exemplo:
        Se n = 7 e a sequência é 6; -2; 7; 0; -5; 8; 4, a saída deve ser
        25.
    Faça ao menos uma simulação passo a passo da execução de
    sua solução.
"""
n = int(input('Informe n: ')) # variaveis são indepentendes. o n de dentro da função, é uma variavel local a função, a modificação será para esta variavel.
soma = 0
cont = 0

while cont < n: # é a quantidade de vezes que eu vou contar (somar)
    sequencia = int(input('Informe um digito da sequencia a ser somada: '))
    
    if sequencia > 0:
        soma = soma + sequencia
    cont += 1
print('A soma dos inteiros informados na sequencia é %d' %(soma))

exit(0)