# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Escreva um programa que recebe as 4 notas bimestrais de um
aluno e mostra a média dessas notas.
"""

nota1 = float(input('1º Nota: '))
nota2 = float(input('2º Nota: '))
nota3 = float(input('3º Nota: '))
nota4 = float(input('4º Nota: '))

soma = nota1 + nota2 + nota3 + nota4
media = soma / 4
print(f'Média do aluno: {media:.1f}')

exit(0)