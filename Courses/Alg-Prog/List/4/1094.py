# !/usr/bin/env python3
# -*- coding: utf-8 -*-

n = int(input())

total_cobaias = 0
quantidade_coelho = 0
quantidade_ratos = 0
quantidade_sapos = 0
while n > 0:

    quantidade_cobaias, tipo_cobaia = input().split()
    quantidade_cobaias = int(quantidade_cobaias)

    total_cobaias += quantidade_cobaias

    if tipo_cobaia == 'C':
        quantidade_coelho += quantidade_cobaias
    
    elif tipo_cobaia == 'R':
        quantidade_ratos += quantidade_cobaias
    
    else:
        quantidade_sapos += quantidade_cobaias

    n -= 1
percentual_coelho = (quantidade_coelho * 100) / total_cobaias
percentual_ratos = (quantidade_ratos * 100) / total_cobaias
percentual_sapos = (quantidade_sapos * 100) / total_cobaias


print(f'Total: {total_cobaias} cobaias')
print(f'Total de coelhos: {quantidade_coelho}')
print(f'Total de ratos: {quantidade_ratos}')
print(f'Total de sapos: {quantidade_sapos}')
print(f'Percentual de coelhos: {percentual_coelho:.2f} %')
print(f'Percentual de ratos: {percentual_ratos:.2f} %')
print(f'Percentual de sapos: {percentual_sapos:.2f} %')

exit(0)