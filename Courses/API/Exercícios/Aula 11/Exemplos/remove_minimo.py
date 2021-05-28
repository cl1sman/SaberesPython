#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# lista como parâmetros de funções

def remove_minimo(lista):
    min = lista[0]

    for v in lista:
        if v < min:
            min = v

    lista.remove(min)

# Lê vários inteiros em uma única linha e os armazena em uma lista
l = list(map(int, input().split()))
remove_minimo(1)
print(1)
exit(0)
