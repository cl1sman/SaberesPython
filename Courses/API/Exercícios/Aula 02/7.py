#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Escreva um programa que receba três valores, armazenando-os nas variáveis x; y e
z, e ordene esses valores de modo que, ao final, o menor valor esteja armazenado
na variável x, o valor intermediário esteja armazenado na variável y e o maior valor
esteja armazenado na variável z. Faça a simulação passo a passo da execução de
sua solução.
"""

"""
Ao todo, são 6 possibilidades:
3>2>1 - ok - ok - ok
2>1<3 - ok - ok - ok
3>1<2 - ok - ok - ok

1<2<3 - ok - ok - ok
1<3>2 - ok - ok - ok
2<3>1 - ok - ok - ok
"""

x = float(input())
y = float(input())
z = float(input())

if x > y:
  if y > z:
    print('primeira condição; primeiro item')
    x, y, z = z, y, x
    print(x, y, z)
  
  elif y < z and z > x: # esse teste, deve estar em segundo lugar, porque se não, a terceira opção será satisfeita, sem que a ultimo teste seja feito.
    print('primeira condição; segundo item')
    x, y, z = y, x, z
    print(x, y, z)
  
  elif y < z:
    print('primeira condição; terceiro item')
    x, y, z = y, z, x
    print(x, y, z)

elif x < y:
  if y < z:
    print('segunda condição; primeiro item')
    print(x, y, z)

  elif y > z and z > x:
    print('segunda condição; segundo item')
    x, y, z = x, z, y
    print(x, y, z)

  elif y > z:
    print('segunda condição; terceiro item')
    x, y, z = z, x, y
    print(x, y, z)

exit(0)