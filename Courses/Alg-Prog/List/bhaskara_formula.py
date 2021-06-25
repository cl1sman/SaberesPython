#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

A, B, C = input().split()
A, B, C = float(A), float(B), float(C)


delta = (B**2) - (4*A*C)
if A == 0 or delta < 0:
    print('Impossivel calcular')

elif delta > 0:
    R1 = (-B + (delta)**(1/2)) / (2*A)
    R2 = (-B - (delta)**(1/2)) / (2*A)
    print(f'R1 = {R1:.5f}')
    print(f'R2 = {R2:.5f}')

exit(0)