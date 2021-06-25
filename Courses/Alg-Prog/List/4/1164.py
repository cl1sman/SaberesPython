# !/usr/bin/env python3
# -*- coding: utf-8 -*-

QuantosTestes = int(input())

while QuantosTestes > 0:
    NumeroPerfeito = int(input())

    soma = 0
    i = 1

    while i < NumeroPerfeito:
        if NumeroPerfeito % i == 0:
            soma += i
        i += 1

    if NumeroPerfeito == soma:
        print(f'{NumeroPerfeito} eh perfeito')
    else:
        print(f'{NumeroPerfeito} nao eh perfeito') 

    QuantosTestes -= 1

exit(0)