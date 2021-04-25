#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Matheus Clisman Mariano da Silva
# Trabalho 1
# Professor(a): Nome do(a) professor(a)
#

"""
    DICA:
    o loop tem que parar quando o valor da aposta for 0
    
    caso contrario você tem que comparar o os numeros do sorteio e se
    atender as condições vc multiplica a aposta e divide em notas de
    100 10 e 1
"""

V, N, M = input().split()
# V = VALOR DA APOSTA
# N = NÚMERO
# M = NÚMERO SORTEADO
V, N, M = int(V), int(N), int(M)

if (N % 10) == (M % 10):
    print(f'Unidades iguais N = {N % 10} e  M = {M % 10}')
    UnidadeN = N % 10
    UnidadeM = M % 10 
    N = N // 10
    M = M // 10

    if (N % 10) == (M % 10):
        print(f'Dezenas iguais N = {N % 10} e  M = {M % 10}')
        dezenaN = N % 10
        dezenaM = M % 10
        N = N // 10
        M = M // 10
        if (N % 10) == (M % 10):
            print(f'Centenas iguais N = {N % 10} e  M = {M % 10}')
            centenaN = N % 10
            centenaM = M % 10
            N = N // 10
            M = M // 10
            print(V * 50)
            if (N % 10) == (M % 10):
                print(f'Dezenas iguais N = {N % 10} e  M = {M % 10}')
                denezaN = N % 10
                dezenaM = M % 10
                N = N // 10
                M = M // 10
                print(V * 500)
                if (N % 10) == (M % 10):
                    print(f'Milhares iguais N = {N} e  M = {M}')
                    milharN = N % 10
                    milharM = M % 10
                    N = N // 10
                    M = M // 10
                    print(V * 3000)
