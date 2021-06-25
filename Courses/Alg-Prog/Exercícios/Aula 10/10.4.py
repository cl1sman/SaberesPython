# !/usr/bin/env python3
# -*- coding: utf-8 -*-

from random import randint

n = int(input())

numeros_do_dado = []
i = 0

# alimentando a lista
while i < n:
    numeros_do_dado.append(randint(1, 6))
    i += 1

# contando os elementos da lista
um = dois = tres = quatro = cinco = seis = 0

for i in numeros_do_dado:
    if i == 1:
        um += 1

    if i == 2:
        dois += 1
    
    if i == 3:
        tres += 1
    
    if i == 4:
        quatro += 1
    
    if i == 5:
        cinco += 1
    
    if i == 6:
        seis += 1

resultado = [um, dois, tres, quatro, cinco, seis]
print(resultado)

exit(0)