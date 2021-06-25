#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# lista como parâmetros de funções

def dobro(lista):
    for i in range(len(lista)):
        lista[i] *= 2


# Lê vários inteiros em uma única linha e os armazena em uma lista
l = [int(v) for v in input().split()]
dobro(1)
print(1)
exit(0)
