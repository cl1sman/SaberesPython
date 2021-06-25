#!/usr/bin/env python3
# -*- coding: utf-8 -*-

start, end = input().split()
start, end = int(start), int(end)

if start < end:
    hora = end - start
else:
    hora = end + 24 - start
print(f'O JOGO DUROU {hora} HORA(S)')

"""
start, end = input().split()
start, end = int(start), int(end)

if start < end:
    print(f'O JOGO DUROU {end - start} HORA(S)') # tirando a diferença, eu sei quanto tempo

elif start == end: # se começar e terminar na mesma hora, provavelmente passou 24 horas, ou ele voltou no tempo :D
    print(f'O JOGO DUROU {24} HORAS(S)')

else:
    print(f'O JOGO DUROU {(24 - start) + end} HORA(S)')
"""
exit(0)