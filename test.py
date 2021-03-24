#!/usr/bin/env python3
# -*- coding: utf-8 -*-


x = 1

while x != 2:
   h = float(input('qual sua altura?: '))

   p1 = (72.7 * h) - 58
   p2 = (62.1 * h) - 44.7

   print('peso recomendado se for homem:', p1)
   print('peso recomendado se for mulher:', p2)

   x = int(input('Deseja continuar: 1 - Sim 2 - Não: '))