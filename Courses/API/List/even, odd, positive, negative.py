# -*- coding: utf-8 -*-

A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())

par = 0
impar = 0
positivo = 0
negativo = 0

# teste para A
if A % 2 == 0: # par
    par +=1
else:
    impar +=1

if A > 0:
    positivo += 1
elif A < 0:
    negativo += 1

# teste para B
if B % 2 == 0: # par
    par +=1
else:
    impar +=1

if B > 0:
    positivo += 1
elif B <0:
    negativo += 1

# teste para C
if C % 2 == 0: # par
    par +=1
else:
    impar +=1

if C > 0:
    positivo += 1
elif C < 0:
    negativo += 1

# teste para D
if D % 2 == 0: # par
    par +=1
else:
    impar +=1

if D > 0:
    positivo += 1
elif D < 0:
    negativo += 1

# teste para E
if E % 2 == 0: # par
    par +=1
else:
    impar +=1

if E > 0:
    positivo += 1
elif E < 0:
    negativo += 1

print(f'{par} valor(es) par(es)')
print(f'{impar} valor(es) impar(es)')
print(f'{positivo} valor(es) positivo(s)')
print(f'{negativo} valor(es) negativo(s)')