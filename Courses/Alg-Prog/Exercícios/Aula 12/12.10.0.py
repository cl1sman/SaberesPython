#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Grupo D
# Adriel Fialho, Larissa Marques, Matheus Clisman, Pedro Alencar
# Exercício 10
# Lista 12
# Professor(a): Diego Rubert

import matplotlib.pyplot as plot
import networkx as nx


def mostra_matriz(matriz):  # Imprime a imagem do "mapa"
    print()
    for i, cidade in enumerate(matriz):
        print("City {} = {}".format(i, cidade))
    print()


def map(cidades):
    print("Digite como ficará o seu Mapa: ")
    matriz = [[int(j) for j in input().split()] for c in range(cidades)]
    mostra_matriz(matriz)
    return matriz


def alt_a(k, matriz):
    soma_saida_city = -1
    for itens_linha in matriz[k]:
        soma_saida_city += itens_linha
    soma_entrada_city = -1
    for linha in matriz:
        soma_entrada_city += linha[k]
    return soma_saida_city, soma_entrada_city


def alt_b(matriz):
    city_more_entradas = []
    quant_entradas = 0
    for city in range(len(matriz)):
        soma_entradas = 0
        for linhas in matriz:
            soma_entradas += linhas[city]
        if soma_entradas == quant_entradas:
            city_more_entradas.append("City {}".format(city))
        elif soma_entradas > quant_entradas:
            city_more_entradas.clear()
    return city_more_entradas


def alt_c(k, matriz):
    mao_dupla = []
    for j, item in enumerate(matriz[k]):
        if item == 1 and k != j:
            if matriz[k][j] == matriz[j][k]:
                mao_dupla.append("City {}".format(j))
    return mao_dupla


def alt_d(k, matriz):
    saida_city = []
    for i, linha in enumerate(matriz):
        if linha[k] == 1 and k != i:
            saida_city.append("Cidade: {}".format(i))
    return saida_city


def alt_e(matriz):
    nenhuma_entrada = []
    nenhuma_saida = []
    for coluna in range(len(matriz)):
        soma_coluna = 0
        for i, linha in enumerate(matriz):
            soma_coluna += linha[coluna]
            soma_linha = 0
            for item in linha:
                soma_linha += item
            if soma_linha == 1:
                if "Cidade {}".format(i) not in nenhuma_saida:
                    nenhuma_saida.append("Cidade {}".format(i))
        if soma_coluna == 1:
            nenhuma_saida.append("Cidade {}".format(coluna))
    isolados = []
    for item in nenhuma_saida:
        if item in nenhuma_entrada:
            isolados.append(item)
    return nenhuma_saida, nenhuma_entrada, isolados


def alt_f(matriz):
    m = [int(x) for x in input("Digite uma Rota para a sua viagem: ").split()]
    rota_viagem = True
    for number in range(len(m) - 1):
        if matriz[m[number]][m[number + 1]] != 1:
            rota_viagem = False
    return rota_viagem, m


def alt_g(matriz, cidades, cidade_k, cidade_p):
    caminho = [0 if city == cidade_k else -1 for city in range(cidades)]
    fila_examinar_cidades, repetido = [cidade_k], [cidade_k]
    for cidade_x in fila_examinar_cidades:
        for cidade_vizinha_x in range(cidades):
            if matriz[cidade_x][cidade_vizinha_x] == 1 and cidade_vizinha_x not in repetido:
                caminho[cidade_vizinha_x] = cidade_x
                fila_examinar_cidades.append(cidade_vizinha_x)
                repetido.append(cidade_vizinha_x)
    rota_entre_cidade = [cidade_k]
    while caminho[cidade_p] != [cidade_k]:
        rota_entre_cidade.append(caminho[cidade_p])
    return caminho, rota_entre_cidade


def mostrar_mapa(matriz):
    cidades = len(matriz)
    image = nx.DiGraph()
    for city in range(cidades):
        image.add_node(city)
    for linha in range(cidades):
        for coluna in range(cidades):
            if matriz[linha][coluna] == 1:
                image.add_edge(linha, coluna)
    pos = nx.circular_layout(image)
    nx.draw(image, pos, with_labels=True, node_color='#CCCCCC')
    plot.show()
    return


def main():
    cidades = int(input("Digete o nª de Cidades que haverá: "))
    k = int(input("Digite o nª da Cidade que deseja examinar: "))
    matriz = map(cidades)
    soma_saida_city, soma_entrada_city = alt_a(k, matriz)
    print("-=-" * 30)
    print("Letra A:")
    print("Na Cidade {} existem {} saídas para outras cidades.".format(k, soma_saida_city))
    print("Na Cidade {} existem {} entradas para outras cidades.".format(k, soma_entrada_city))
    city_more_entradas = alt_b(matriz)
    print("-=-" * 30)
    print("Letra B:")
    print("As Cidades com maior(es) Nº de ENTRADAS: ")
    for citys in city_more_entradas:
        print("- {}".format(citys))
    mao_dupla = alt_c(k, matriz)
    print("-=-" * 30)
    print("Letra C:")
    if mao_dupla:
        print("As Cidades que fazem ligação de 'MÂO DUPLA' com a CIDADE {} são:".format(k))
        for city in mao_dupla:
            print("-  {}".format(city))
    else:
        print("Não existe NENHUMA Cidade que se liga com 'MÂO DUPLA' com a CIDADE {}".format(k))
    saida_city = alt_d(k, matriz)
    print("-=-" * 30)
    print("Letra D:")
    if saida_city:
        print("As Cidades que tem Saída Direta com a CIDADE {} são:".format(k))
        for city in saida_city:
            print("-  {}".format(city))
    else:
        print("NENHUMA Cidade que tem Saída Direta com a CIDADE {}".format(k))
    nenhuma_saida, nenhuma_entrada, isolados = alt_e(matriz)
    print("-=-" * 30)
    print("Letra E:")
    print("Cidades que NÃO possuem SAÍDA: {}".format(nenhuma_saida))
    print("Cidades que NÃO possuem ENTRADA: {}".format(nenhuma_entrada))
    print("Cidades que estão ISOLADAS: {}".format(isolados))
    print("-=-" * 30)
    print("Letra F:")
    rota_viagem, sequencia_m = alt_f(matriz)
    if rota_viagem:
        print("Dada a Sequência {}, EXISTE um ROTA para viajar.".format(sequencia_m))
    else:
        print("Infelizmente a Sequência {} NÃO possui uma ROTA para viajar.".format(sequencia_m))
    print("-=-" * 30)
    print("Letra G:")
    p = int(input("Digite em que Cidade você gostaria de encontrar o caminho mais rápido: "))
    caminho, rota_entre_cidades = alt_g(matriz, cidades, k, p)
    if k == p:
        print('A Cidade {} e a Cidade {} são as mesmas, tente novamente mais tarde !!'.format(k, p))

    elif caminho[p] == -1:
        print('Não existe caminho entre as Cidade {} e a Cidade {}'.format(k, p))

    else:
        print('O menor caminho entre a Cidade {} e a Cidade {} é:'.format(k, p))

        for rota in rota_entre_cidades:
            print("Cidade {} -> ".format(rota), end='')
        print("Cidade {}".format(p))
    print("-=-" * 30)
    mostrar_mapa(matriz)


if __name__ == '__main__':
    main()

#------------------------------------------------------------------------------------|:::::::::::::|---------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------| < THE END > |---------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------|:::::::::::::|---------------------------------------------------------------------------------------------------