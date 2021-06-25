#!/usr/bin/env phyton3
#-*-coding: utf-8 -*-


# resto da divisão por 10
"""
Eu fui pegando cada digito e printando, só qeu dai no print 
botei um end e virou o numero só que invertido
"""

numero = int(input())
resto = 0

while numero > 9: # 9, porque não há digito maior que nove, quando chegar em um unico digito, ele será coparado a 9. exe. 2 > 9 ou 9 > 9, não sendo mais verdadeiro;]
    ultimodigito = numero % 10 # pego o ultimo digito

    # faço a soma, antes de multiplicar
    resto += ultimodigito
    # faço a multiplicação, para acrescentar um zero a direita. de 8, passa a ser 80
    resto *= 10
    # por fim, eu elimino o ultimo digito
    numero //= 10

numeroinvertido = resto + numero # somo com numero, porque sempre vai sobrar um digito.
print(numeroinvertido)
exit(0)