#!/usr/bin/env python3
# -*- coding: utf-8 -*-

valor = list(map(int, input().split()))

i = 0
soma = 0

while i < valor[-1]:
    soma = soma + (valor[0] + i)
    i += 1
print(soma)

exit(0)