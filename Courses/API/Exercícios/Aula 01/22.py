#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Faça um programa que após a entrada de uma determinada
distância entre dois pontos (em Km) e uma determinada
velocidade (Km/h), diga qual o tempo médio que levará para
chegar a esse local e qual a velocidade em metros/segundos.
"""
distancia = float(input('Distancia em Km '))
velocidade = float(input('Velocidade Km/h '))

tempo_medio = distancia / velocidade
velocidade_kmh_para_ms = velocidade / 3.6

print(f'Tempo médio: {tempo_medio}')
print(f'Velocidade em metros/segundo: {velocidade_kmh_para_ms:.2f}')

exit(0)