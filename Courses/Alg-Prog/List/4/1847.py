# !/usr/bin/env python3
# -*- coding: utf-8 -*-

A, B, C = input().split()
A, B, C = float(A), float(B), float(C)

if A > B and B <= C:
    print(':)')
elif A < B and B >= C:
    print(':(')
elif A < B and B < C:
    if (B - A) > (C - B):
        print (":(")
    elif (B - A) <= (C - B):
        print(':)')
elif A > B and B > C:
    if (A - B) > (B - C):
        print(':)')
    elif (A - B) <= (B - C):
        print(':(')
elif A == B and B < C:
    print(':)')
else:
    print(':(')
exit(0)