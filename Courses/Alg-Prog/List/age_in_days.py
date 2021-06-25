# !/usr/bin/env python3
# -*- coding: utf-8 -*-

age = int(input('Idade em dias: '))
anos = int(age / 365) # ou age // 365
meses = int((age % 365) / 30) # vai pegar age, dividir por 365 e retornar o resto da divisão, o resto da divisão será dividido por 30
dias = int((age % 365) % 30) # int, vai dispensar a parte quebrada, levando em consideração apenas a parte inteira.

print(f'{anos} ano(s)')
print(f'{meses} mes(es)')
print(f'{dias} dia(s)')

exit(0)