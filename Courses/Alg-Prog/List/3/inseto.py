# !/usr/bin/env python3
# -*- coding: utf-8 -*-

C = int(input()) # número de casos de testes

while C > 0:
    N = int(input())
    if N <= 8000:
        print('Inseto!')
    else:
        print('Mais de 8000!')
    C -= 1

exit(0)