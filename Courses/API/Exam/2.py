"""
Escreva uma função que receba 3 inteiros e devolva dois inteiros: o menor e o maior valor dentre os três recebidos. Não é permitido o uso da funções min e maa ou qualquer outra função ou classe. Use apenas inteiros e estruturas condicionais if (opcionalmente junto com elif ou else).

Escreva *apenas* a função, e use a seguinte definição:
"""

def menor_e_maior(x, y, z):

  if x > y:
    x, y = y, x
  if x > z:
    x, z = z, x
  if y > z:
    y, z = z, y

  menor, maior = x, z
  return menor, maior
# Esse código será executado fora da função
x,y,z = input().split()
x,y,z = int(x),int(y),int(z)
menor,maior = menor_e_maior(x, y, z)
print(menor, maior)