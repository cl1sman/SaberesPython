"""
num = list(map(str, input("Digite uma sequência de inteiros:  ").split()))

menor = num[0]
i = 1
x = len(num) - 1

while i < x:
    if num[i] < num[0+1]:
        num[i], num[0] = num[0], num[i]
    i += 1
print (num)

#########
num = list(map(str, input("Digite uma sequência de inteiros:  ").split()))

menor = num[0]
i = 0

while i < len(num) - 1:
    if num[i] < num[i+1]:
        num[i], num[i+1] = num[i], num[i+1]
    else:
        num[i], num[i+1] = num[i+1], num[i]
    i += 1
print (num)
"""

# !/usr/bin/env python3
# -*- coding: utf-8 -*-

num = list(map(str, input("Digite uma sequência de inteiros:  ").split()))

menor = num[0]
i = 0

while i < len(num) - 1:
    if num[i] < num[i+1]:
        num[i], num[i+1] = num[i], num[i+1]
    else:
        num[i], num[i+1] = num[i+1], num[i]
    i += 1
print (num)
exit(0)