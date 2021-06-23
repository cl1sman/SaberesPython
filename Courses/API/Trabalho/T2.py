# [x] quadra
# [x] Full House
# [x] converter em valores J, Q, K, A
# [x] problema com 10 para sequencia
# [] trinca

"""
para o problema do 10, porque ele vai pegar o primeiro item
v[-1]
if v[0]  == "1":
  valor_carta = int(10)

elif v[0] == "J":
     valor_carta = int(10)
..........

elif v[0] == "A":
     valor_carta = int(14)

else:
    valor_carta = int(v[0])
"""

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

"""
jogador1 = input().split()

# Trinca: 3 cartas com o mesmo valor
def trinca(cartas):
    if cartas.count(int(cartas[0][0])) == 2:
        return True

if trinca(jogador1):
    print('Sequencia')
"""

k = int(input()) # quantidade de casos de teste

for i in range(k):
    jogador1 = input().split()
    jogador2 = input().split()


# testes:
if quadra(jogador1):
    print('JOGADOR 1 TEM UMA QUADRA')
elif full_house(jogador1):
    print('JOGADOR 1 TEM UM FULL HOUSE')
elif flush(jogador1):
    print('JOGADOR 1 TEM UM FLUSH')
elif sequencia(jogador1):
    print('JOGADOR 1 TEM UMA SEQUENCIA')