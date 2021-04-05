#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Dadas duas cadeias de caracteres cadeia1 e cadeia2 ,
compará-las e escrever -1 se cadeia1 é lexicograficamente
menor que cadeia2 , o 0 se cadeia1 é igual ou tem o mesmo
conteúdo que cadeia2 , ou 1 se cadeia1 é lexicograficamente
maior que cadeia2 . Seu programa deve ignorar a caixa das
letras, ou seja, as cadeias teste e Teste devem ser
consideradas iguais por exemplo.
"""
cadeia1 = input().lower()
cadeia2 = input().lower()

if cadeia1 < cadeia2:
    print(-1)

elif cadeia1 == cadeia2:
    print(0)

else:
    print(1)

exit(0)