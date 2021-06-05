#!/usr/bin/env python3
# -*- coding: utf-8 -*-

n = []
i = 0

while i < 20:
    n.append(int(input()))
    i += 1

a = []
i = - 1
while i >= - 20:
    a.append(n[i])
    i -= 1
n = a.copy()

for j in range(20):
    print(f'N[{j}] = {n[j]}')
exit(0)