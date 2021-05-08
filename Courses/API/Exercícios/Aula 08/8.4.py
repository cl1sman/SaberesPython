#!/usr/bin/env phyton3
#-*-coding: utf-8 -*-

numero = int (input())

binario = 0
i = numero
pot = 1

while i > 0:
    # usando o mesmo esquema de resto e divisão inteira
    digito = i % 2
    i = i // 2
    binario += + digito * pot
    pot *= 10

print ("o número %d na base binária é %d" % (numero, binario))

exit (0)