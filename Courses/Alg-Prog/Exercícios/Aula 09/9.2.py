#!/usr/bin/env phyton3
#-*-coding: utf-8 -*-

# SEQUÊNCIA DE FIBONACCI


def Fib(n):
    i = 0
    anterior = 1
    atual = 1
    print(anterior)
    print(atual)
    while i < (n-2):
        soma = anterior + atual
        atual, anterior = soma, atual
        print(atual)

        i += 1

n = int(input())
Fib(n)

exit(0)