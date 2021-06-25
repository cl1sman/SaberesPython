#!/usr/bin/env python3
# -*- coding: utf-8 -*-

n = int(input('Digite a quantidade de notas: '))

notas = []

for i in range(n):
    notas.append(float(input()))

media = 0.0

for nota in notas:
    media += nota
media /= n

menor = maior = 0
for nota in notas:
    if nota < media:
        menor += 1
    if nota >= media:
        maior += 1

print('Media: %2.2f, %d menores e %d maiores', media, menor, maior)
print(f'Media: {media:.2f}, {menor} menores e {maior} maiores')
