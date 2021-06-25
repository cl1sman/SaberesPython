#!/usr/bin/env python3
# -*- coding: utf-8 -*-

x = float(input())
n = []

for i in range(100):
    n.append(x)
    x /= 2
    print(f'N[{i}] = {n[i]:.4f}')

exit(0)