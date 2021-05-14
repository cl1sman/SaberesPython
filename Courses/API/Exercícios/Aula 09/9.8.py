#!/usr/bin/env phyton3
#-*-coding: utf-8 -*-

n = 0
pi = 0
valorabs = 1
soma = 0

while valorabs > 0.00001: # com um zero a mais, chego a 3,1415(...). Com apenas 3 zeros, chego em 3,141643(...)
    pi = 4 * ((-1)**n) / (2*n + 1) # 4 - 4/3 + 4/5 - 4/7 + 4/9 ...
    soma = soma + pi
    valorabs = abs(pi)
    n += 1

print('%.4f' %soma) # essa coisa arredonda
truncado = int(soma * 10**4) / (10**4)
print(truncado)

exit(0)