# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    Escreva um programa que leia 2 valores X e Y 
    e que imprima todos os valores entre eles cujo 
    resto da divisão dele por 5 for igual a 2 ou 
    igual a 3.
"""

X = int(input())
Y = int(input())

if X > Y:
    X, Y = Y, X

X += 1
while X < Y:
    if X % 5 == 2 or X % 5 == 3:
        print(X)
    X += 1

exit(0)