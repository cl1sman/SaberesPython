#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# Matheus Clisman Mariano da Silva
# Trabalho 1
# Professor(a): Diego Padilha Rubert
#

"""
    DICA:
    o loop tem que parar quando o valor da aposta for 0
    
    caso contrario você tem que comparar o os numeros do sorteio e se
    atender as condições vc multiplica a aposta e divide em notas de
    100 10 e 1
"""
import math

V, N, M = input().split()
# V = VALOR DA APOSTA
# N = NÚMERO apostasdo
# M = NÚMERO SORTEADO
V, N, M = int(V), int(N), int(M)

# def # do notas e moedas do URI
def grupo_dos_bichos(v, n, m):

    if  n % 10000 == m % 10000: # para testar os ultimos 4 digitos
        v = v * 3000
    
    elif  n % 1000 == m % 1000:
        v = v * 500
    
    elif n % 100 == m % 100:
        v = v * 50
    
    else: # coloquei as duas ultimas condições em uma. se a penultima não for satisfeita, ela faz a ultima
        n = n % 100
        m = m % 100

        if n == 00:
            n = 100
        
        elif m == 00:
            m = 100
        
        x = math.ceil(n / 4)
        y = math.ceil(m / 4)
        
        if x == y:
            v = v * 16
        
        else:
            v = 0

    return v

def money(v):
    pila100 = v // 100
    resto = v % 100
    
    pila10 = resto // 10
    pila1 = resto % 10


    return (f'{v} {pila100}x100 {pila10}x10 {pila1}x1') 

aposta = grupo_dos_bichos(V, N, M)
premio = money(aposta)

print(premio)