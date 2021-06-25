#!/usr/bin/env python3
# -*- coding: utf-8 -*-
A, B, C = input().split()
A, B, C = int(A), int(B), int(C)
D = A
E = B
F = C

if A > B:
  if B > C:
    A, B, C = C, B, A
    print(A)
    print(B)
    print(C)
  
  elif B < C and C > A: # esse teste, deve estar em segundo lugar, porque se não, a terceira opção será satisfeita, sem que a ultimo teste seja feito.
    A, B, C = B, A, C
    print(A)
    print(B)
    print(C)
  
  elif B < C:
    A, B, C = B, C, A
    print(A)
    print(B)
    print(C)

elif A < B:
  if B < C:
    print(A)
    print(B)
    print(C)

  elif B > C and C > A:
    A, B, C = A, C, B
    print(A)
    print(B)
    print(C)

  elif B > C:
    A, B, C = C, A, B
    print(A)
    print(B)
    print(C)

print()
print(D)
print(E)
print(F)

exit(0)