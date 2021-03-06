def velocidade_media(distancia, tempo): # distancia em metros, e tempo em segundos
    velocidade = distancia / tempo
    return velocidade

def soma(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def calculadora(x, y):
    return x+y, x-y, x*y, x/y


print(calculadora(4, 5))