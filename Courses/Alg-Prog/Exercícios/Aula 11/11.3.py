#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def intersec(A, B):
    nova_lista = []
    for i in A:
        if i in B:
            if i not in nova_lista:
                nova_lista.append(i)
    return nova_lista

A = [int(v) for v in input().split()]
B = [int(v) for v in input().split()]

interseção = intersec(A, B)
print(interseção)
exit(0)