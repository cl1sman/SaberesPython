#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Escreva um programa que recebe o tamanho de um arquivo para
download (em MB) e a velocidade de um link de internet (em
Mbps), calcula e informa o tempo aproximado de download do
arquivo usando este link (em minutos).
"""
tamanho_do_arquivo = float(input('Tamanho do arquivo em MB: '))
velocidade_internet = float(input('Velocidade da internet em Mbps: '))

tempo_aproximado = ((tamanho_do_arquivo * 8) / velocidade_internet) / 60
print(f'Tempo aproximado de download do arquivo {tamanho_do_arquivo}, com velocidade {velocidade_internet}, levará: {tempo_aproximado:.5f} min')

exit(0)