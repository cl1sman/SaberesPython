# -*- coding: utf-8 -*-

A, B = int(input().split()), int(input().split())

if (A % B == 0) or (B % A == 0):
    print('Sao Multiplos')

else:
    print('Nao sao Multiplos')


# uma solução de alguém que encontrei
"""
a, b = int(input().split())

if a > b and a % b == 0:
  print('Sao Multiplos')

elif a < b and b % a == 0:
  print('Sao Multiplos')

elif a % b != 0 or b % a != 0:
  print('Não sao multiplos')
 
exit(0)
"""