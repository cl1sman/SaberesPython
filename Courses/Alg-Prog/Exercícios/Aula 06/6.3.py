#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
3. 
    (a) Escreva uma função com a seguinte interface: 
        def idade_em_dias(anos, meses, dias):
    que receba a idade de uma pessoa em anos, meses e dias e
    devolva essa idade expressa em dias.
    
    (b) Escreva um programa que receba leia a idade de uma pessoa em
    anos, meses e dias e escreva essa idade em dias. Utilize a função
    acima.
"""

def idade_em_dias(anos, meses, dias):
    return ((365 * anos) + (meses * 30) + dias)

anos = int(input('Anos: '))
meses = int(input('Meses: '))
dias = int(input('Dias: '))
print(idade_em_dias(anos, meses, dias))

exit(0)