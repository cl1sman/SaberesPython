#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    O programa abaixo pretende resolver o seguinte problema computacional: dado um número inteiro positivo n, somar os n primeiros inteiros positivos.
"""

n = int(input('Informa n: '))
soma = 0
numero = 1
while numero <= n:
    soma = soma + numero
    numero = numero + 1
print('Soma dos %d primerios inteiros é %d' % (n, soma))
exit(0)

"""
    Verifique se tal solução está correta. Faça algumas simulações passo a passo da execução do programa.
"""