"para retornar múltiplos valores, retornamos os resultados separados por vírgula"

def calculadore(x, y):
    return x+y, x-y "o tipo de retorno desta função é <class 'tuple'>"


"outra maneira, com o retorno retornando um dicionário"
def calculadora(x, y):
    return {'soma': x+y, 'subtração': x-y}

resultados = calculadora(1, 2)
for key in resultados:
    print('{}: {}'.format(key, resultados[key]))