"""
Os pontos (x; y) que pertencem à figura H são tais que
x > 0; y > 0 e x2 + y2 6 1. Dados um ponto real (x; y), verifique se
pertence ou não a H.
"""

x = float(input())
y = float(input())

if (x >= 0) and (y >= 0) and (x**2 + y**2 <= 1):
    print('Pertence a H')
else:
    print('Não pertence')