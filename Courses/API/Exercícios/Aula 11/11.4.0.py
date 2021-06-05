#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def uns(contadores):
	for valor in contadores:
		if valor != 1:
			return False
	return True # não achei nenhum

sequencia = [int(v) for v in input().split()]
# olhar par a par
n = len(sequencia)
# contadores = [0] * (n-1) # se tem n elementos, tereis n-1 pares
contadores = [0]*n
contadores[0] = 1

for i in range(1, n): # [1, n-1]
	diferença = abs(sequencia[i-1] - sequencia[i])
	if diferença < n:   # 100 50 20
		contadores[diferença] += 1

if uns(contadores):
	print('Cheia')
else:
    print('Não é cheia')

exit(0)