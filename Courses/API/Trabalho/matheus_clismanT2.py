# [x] quadra
# [] Full House
# [] converter em valores J, Q, K, A
# [] problema com 10

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

k = int(input()) # quantidade de casos de teste

for i in range(k):
    jogador1 = input().split()
    jogador2 = input().split()


# teste se quadra:
if quadra(jogador1):
    print('JOGADOR 1 TEM UMA QUADRA')
if full_house(jogador1):
    print('JOGADOR 1 TEM UM FULL HOUSE')