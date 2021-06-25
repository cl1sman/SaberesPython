#!/usr/bin/env python3
# -*- coding: utf-8 -*-


####################################################
# input:                                           #
#                                                  #
#   5E 7O 8O JO AC                                 #
#   2P 2C 4E 6O 7P                                 #
#   Output:  2                                     #
#                                                  #
#   5O 5P 5C 9C 9E                                 #
#   6E 6O KE KO KC                                 #
#   Output: E                                      #
#                                                  #
#   3P 6P 7O 9C JE                                 #
#   2E 3E 4E 5E 10C                                #
#   Output: 1                                      #
#                                                  #
#   2P 5O 7P 10C KC                                #
#   3P 4C 6P 9O KE                                 #
#   Output: E                                      #
#                                                  #
#   8C 9C 10O JP QE                                #
#   3E 4E 5E 6E 7E                                 #
#   Output: 2                                      #
#                                                  #
#   2O 3O 4P 5C 6O                                 #
#   10C JC QC KC AP                                #
#   Output: E                                      #
#                                                  #
####################################################

# FUNÇÕES
def quadra(cartas):
    cont = 0
    # ['2P', '2E', '2P', '2E', '5F']
    # caso o primeiro e segundo elementos sejam iguais
    if cartas[0][0] == cartas[1][0]:
        teste = cartas[0][0]
        for i in range(1, 4):
            atual = cartas[i][0]
            if atual == teste:
                cont += 1
    # '5O', '2P', '2E', '2P', '2E'
    # caso o primeiro e o segundo serem diferentes
    else:
        teste = cartas[1][0]
        for i in range(2, 5):
            atual = cartas[i][0]
            if atual == teste:
                cont += 1
        
    if cont == 3:
        return True
    else:
        return False

def full_house(cartas):
    # '2P', '2E', '2P', '5E', '5F'
    # caso os três primeiros sejam iguais
    if cartas[0][0] == cartas[1][0] == cartas[2][0] and cartas[3][0] == cartas[4][0]:
        return True
            
    # '5O', '2P', '2E', '2P', '2E'
    # caso os três ultimos forem iguais
    elif cartas[0][0] == cartas[1][0] and cartas[2][0] == cartas[3][0] == cartas[4][0]:
        return True

def flush(cartas):
    # '2F', '2F', '2F', '5F', '5F'
    if cartas[0][-1] == cartas[1][-1] == cartas[2][-1] == cartas[3][-1] == cartas[4][-1]:
        return True

def sequencia(cartas):
    soma = 0
    nova_list = []
    for remover in cartas:
        nova_list.append(remover[:-1]) # remover o ultimo elemento
        
    
    for item in range(5):
        if 'J' in nova_list[item]:
            nova_list[item] = 11
        elif 'Q' in nova_list[item]:
            nova_list[item] = 12
        elif 'K' in nova_list[item]:
            nova_list[item] = 13
        elif 'A' in nova_list[item]:
            nova_list[item] = 14
        
    
    for i in range(5):
        soma += int(nova_list[i])
    
    if nova_list[0] == '2':
        if soma == 20:
            return True
    elif nova_list[0] == '3':
        if soma == 25:
            return True
    elif nova_list[0] == '4':
        if soma == 30:
            return True
    elif nova_list[0] == '5':
        if soma == 35:
            return True
    elif nova_list[0] == '6':
        if soma == 40:
            return True
    elif nova_list[0] == '7':
        if soma == 45:
            return True
    elif nova_list[0] == '8':
        if soma == 50:
            return True
    elif nova_list[0] == '9':
        if soma == 55:
            return True
    if nova_list[0] == '10':
        if soma == 60:
            return True

def trinca(cartas):
    # 2C 2E 2O 4C 5C
    if cartas[0][0] == cartas[1][0] == cartas[2][0] and cartas[3][0] != cartas[4][0]:
        return True
    
    # 2C 3E 4C 4E 4O
    elif cartas[0][0] != cartas[1][0] and cartas[2][0] == cartas[3][0] == cartas[4][0]:
        return True
    
    # 2E 3C 3O 3P 5C
    elif (cartas[1][0] == cartas[2][0] == cartas[3][0]):
        if cartas[0][0] != (cartas[1][0] == cartas[2][0] == cartas[3][0]):
            if (cartas[1][0] == cartas[2][0] == cartas[3][0]) != cartas[4][0]:
                return True

def twopares(cartas):
    # 2C 2P 3O 3E 4C
    # 2C 4E 4O 7P 7C
    # 3C 3E 5O 7P 7E
    par = 0
    for i in range(4):
        atual = cartas[i][0]
        proximo = cartas[i+1][0]
        if atual == proximo:
            par += 1
    if par == 2:
        return True

def par(cartas):
    # 2C 2E 3P 4E 5C
    # 2C 3E 3C 4O 5P
    # 2C 3E 4C 4E 5P
    # 2C 3E 4P 5C 5O

    par = 0
    for i in range(4):
        atual = cartas[i][0]
        proximo = cartas[i+1][0]
        if atual == proximo:
            par += 1
    if par == 1:
        return True

def alta(cartas):
    nova_list = []
    for remover in cartas:
        nova_list.append(remover[:-1]) # remover o ultimo elemento
        
    
    for item in range(5):
        if 'J' in nova_list[item]:
            nova_list[item] = 11
        elif 'Q' in nova_list[item]:
            nova_list[item] = 12
        elif 'K' in nova_list[item]:
            nova_list[item] = 13
        elif 'A' in nova_list[item]:
            nova_list[item] = 14
    nova_list[-1] = int(nova_list[-1])
    
    return nova_list[-1]

def pontuation(x):
    
    soma = 0
    # testes:
    if quadra(x):
        soma += 7000

    elif full_house(x):
        soma += 6000

    elif flush(x):
        soma += 5000

    elif sequencia(x):
        soma += 4000

    elif trinca(x):
        soma += 3000

    elif twopares(x):
        soma += 2000

    elif par(x):
        soma += 1000
        
    elif alta(x):
        soma += alta(x)
    
    return soma

k = int(input()) # quantidade de casos de teste

# comparação dos jogadores
for i in range(k):
    jogador1 = input().split()
    jogador2 = input().split()

    if pontuation(jogador1) > pontuation(jogador2):
        print('1')

    elif pontuation(jogador1) < pontuation(jogador2):
        print('2')
    else:
        print('E')