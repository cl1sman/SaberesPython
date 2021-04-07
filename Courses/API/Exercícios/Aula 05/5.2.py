"""
Dado um número inteiro n, escreva “SIM” se ele é ao mesmo
tempo par e positivo. Caso contrário, escreva “NÃO”.
"""

n = int(input())

if n % 2 == 0 and n >0: # n % 2 == 0, se um múmero dividido por dois, e o resto da divisão é zero
    print('SIM')
else:
    print('NÃO')