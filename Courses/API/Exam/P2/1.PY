# !/usr/bin/env python3
# -*- coding: utf-8 -*-

sequencia, n  = input().split()
sequencia, n  = int(sequencia), int(n)

i = 0
potencia = 0
while n > i:
    if i == 0:
        potencia = 1
    else:
        potencia *= sequencia
    print(potencia, end=' ')
    i += 1
exit(0)