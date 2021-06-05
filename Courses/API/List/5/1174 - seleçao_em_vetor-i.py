#!/usr/bin/env python3
# -*- coding: utf-8 -*-

n = []
i = 0

while i < 100:
    v = float(input())
    n.append(v)
    if v <= 10:
        print(f'A[{i}] = {n[i]}')

    i += 1

exit(0)