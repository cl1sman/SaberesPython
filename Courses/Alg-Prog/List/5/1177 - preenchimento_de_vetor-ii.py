#!/usr/bin/env python3
# -*- coding: utf-8 -*-

n = []
t = int(input())
i = 0
fim_vetor = 1000

while i < fim_vetor:
    for j in range(t):
        n.append(j)
        print(f'N[{i}] = {n[i]}')
        i += 1
        if i > (fim_vetor - 1):
            break

exit(0)