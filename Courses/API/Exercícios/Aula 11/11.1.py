#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# a) escreva uma função que diga se um conjunto esta contido

def subconjunto(a, b):
    soma = 0
    for i in a:
        if i in b:
            soma += 1
    if soma == len(a):
        return True
    else:
        return False

A = [int(v) for v in input().split()]
B = [int(v) for v in input().split()]

contido = subconjunto(A, B)
print(contido)

# b) se conjuntos são iguais
conjuntos_iguais = subconjunto(A, B) == subconjunto(B, A)

if conjuntos_iguais == True:
    print('conjuntos iguais')
else:
    print('conjuntos não iguais')