#!/usr/bin/env python3
# -*- coding: utf-8 -*-

N = int(input())
A, B = input().split()

if N >= (int(A) + int(B)):
    print('Farei hoje!')
else:
    print('Deixa para amanha!')

exit(0)