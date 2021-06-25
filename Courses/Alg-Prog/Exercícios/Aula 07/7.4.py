#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    Dado um número inteiro positivo n, imprimir as n primeiras
    potências de 2.
        Exemplo:
            Para n = 5 a saída deverá ser 1; 2; 4; 8; 16.
    Faça ao menos uma simulação passo a passo da execução de
    sua solução.
"""
"""
    Uma potência de dois é qualquer número obtido ao elevar o número dois a uma potência inteira não negativa
"""
n = int(input('Informe n: ')) # variaveis são indepentendes. o n de dentro da função, é uma variavel local a função, a modificação será para esta variavel.
numero = 0

while numero < n:
    print(2**numero)
    numero = numero + 1


print('%d primeiras potências de 2 é %d' %(n, numero))
exit(0)