#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Esta função recebe um ano e devolve
# True se o ano for bissexto e False caso contrário
def bissexto(a):
    if a % 400 == 0:
        return True
    if a % 100 == 0:
        return False
    if a % 4 == 0:
        return True
    
    return False
    
    
# NÃO modifique o código abaixo
a = int(input())
if bissexto(a):
    print("O ano %d é bissexto" % a)
else:
    print("O ano %d não é bissexto" % a)
exit(0)