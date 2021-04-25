import math
pontoX1 = int(input('X1: '))
pontoY1 = int(input('Y1: '))

pontoX2 = int(input('X2: '))
pontoY2 = int(input('Y2: '))
distancia_entre_dois_pontos = math.sqrt((pontoX1 - pontoX2)** 2 + (pontoY1 - pontoY2)**2)

if distancia_entre_dois_pontos >= 10:
    print('longe')
else:
    print('perto')