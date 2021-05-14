#!/usr/bin/env phyton3
#-*-coding: utf-8 -*-

a = int(input())
b = int(input())

# while a % 2 == 0 and b % 2 == 0: # condição para ser par
#     a = a // 2
#     b = b // 2

# while a % 3 == 0 and b % 3 == 0:
#     a = a // 3
#     b = b // 3

# print(f'{a}/{b}')

# exit(0)



# # solução do professor
# while mdc(a,b) != 1: # mdc, me da a multiplicação de todos os termos.
#     div = mdc(a,b)
#     a //= div
#     b //= div

# então
div = 2
while div <= a and div <=b: # multiplicação dos varios termos que dividem
    if a%div == 0 and b%div == 0:
        a //= div
        b //= div
    else:
        div += 1

print(f'{a}/{b}')