#!/usr/bin/env phyton3
#-*-coding: utf-8 -*-

n = int(input('Informe um número inteiro positivo: ')) # se o afortunado colocar 0, deu pau no excel.

anterior = int(input(f'Informe a sequencia dom {n} elementos: '))
contador = 1
i = 2
while i <= n:
    atual = int(input('Proximo elemento da sequencia: '))

    if (atual != anterior):
        contador = contador + 1
        anterior = atual
    
    i += 1

print(f'{contador} segmentos de números iguais.')
exit(0)