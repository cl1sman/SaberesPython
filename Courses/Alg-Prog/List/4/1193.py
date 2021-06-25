# !/usr/bin/env python3
# -*- coding: utf-8 -*-


# num = int(input())
# cont = 0
# aux = num
# resto = []
# while aux > 0:
#     dig = aux % 16
#     aux = aux // 16
 
#     resto.append(dig)
#     if aux // 16 == 0:
#         aux = str(aux) # Transformando os valores em string.
#         dig = str(dig) # Transformando os valores em string.
    
#         if int(dig) > 9:
#             hex = aux + chr(int(dig) + 87) + str(resto[0]) # Transformando em hexadecimal com a conversão do num > 9.
#             print(hex)
#             break
#         else: # Se o valor < 9, imprime o hex normal.
#             hex = aux + dig
#             print(hex)
#             break

# numero = int(input())
# aux = numero
# resto = []

# while aux > 0:
#     dig = aux % 16
#     aux = aux // 16

#     resto.append(dig)
# x = len(resto) - 1
# resultado_hex = []

# while (x >= 0):
#     resultado_hex.append(resto[x])
#     x = x -1

# i = 0
# while resto[i] // 16 == 0:



# Decimais
def decimal_binario(numero):
    numero = int(numero)
    valor = ''
    resto = 0

    while True:
        resto = numero // 2
        aux = numero - (resto * 2)

        valor += str(aux)

        numero = numero // 2

        if numero <= 0:
            break
    print(valor[::-1], 'bin')

def decimal_hexa(numero):
    numero = int(numero)
    print(hex(numero)[2:], 'hex')

# Bin
def binario_decimal(numero):
    numero = list(numero)
    valor = 0

    for i in numero:
        valor = valor * 2 + int(i)
    print(valor, 'dec')
def binario_hexa(numero):
    numero = list(numero)
    
    valor = 0

    for i in numero:
        valor = valor * 2 + int(i)
    
    print(hex(valor)[2:], 'hex')

# HEXA
def hexa_decimal(numero):
    numero = int(numero, 16)

    print(numero, 'dec')

def hexa_binario(numero):
    numero = int(numero, 16)
    decimal_binario(numero)

vezes = int(input())

for i in range(vezes):
    numero, base = input().split()
    print('Case %d:'%(i+1))

    if base == 'bin':
        binario_decimal(numero)
        binario_hexa(numero)

    elif base == 'dec':
        decimal_hexa(numero)
        decimal_binario(numero)
    
    elif base == 'hex':
        hexa_decimal(numero)
        hexa_binario(numero)
print()
exit(0)