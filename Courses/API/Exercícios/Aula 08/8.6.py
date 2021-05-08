#!/usr/bin/env phyton3
#-*-coding: utf-8 -*-

"""
    Dizemos que um número natural n é palíndromo se
    o primeiro algarismo de n é igual ao seu último algarismo;
    o segundo algarismo de n é igual ao se penúltimo algarismo
    e assim sucessivamente.
    
    Exemplos:
        567765 é palíndromo
        32423 é palíndromo
        567675 não é palíndromo.
    Dado um número natural n, verificar se n é palíndromo. Faça pelo menos uma
    simulação da execução passo a passo da sua solução.
"""
numero = int(input())

def inverternumero(numero):
    resto = 0
    while numero > 9:
        ultimodigito = numero % 10
        resto += ultimodigito
        resto *= 10
        numero //= 10
        
    return resto + numero
numeroinvertido = inverternumero(numero)

if numero == numeroinvertido:
    print(f'{numero} é palíndromo')
else:
    print(f'{numero} não é palíndromo')
exit(0)