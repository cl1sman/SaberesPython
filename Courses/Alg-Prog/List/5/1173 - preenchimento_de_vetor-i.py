#!/usr/bin/env python3
# -*- coding: utf-8 -*-

n = []
i = 0
v = int(input())
while i < 10:
    n.append(v)
    v = v + v

    print(f'N[{i}] = {n[i]}')

    i += 1

exit(0)