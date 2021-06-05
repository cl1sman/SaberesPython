lista_de_inteiros = [1, 2, 3, 4, 5, 3, 2]
temporario = []

for _ in lista_de_inteiros:
    if _ not in temporario: # não esta no temporario? se não, adiciona
        temporario.append(_)

print(temporario)