valor = float(input())
valor_notas = int(valor)
valor_moedas = int( 100*valor - 100*int(valor) ) 

print(valor_notas, valor_moedas)


if  (valor_notas // 100) != 0:
    n100 = valor_notas // 100
    valor_notas = n100 % 100 # Resto da divisão N %= 100 seria mesmo o resto

elif (valor_notas // 50) != 0:
    n50 = valor_notas // 50
    valor_notas = n50 % 50

elif (valor_notas // 20) != 0:
    n20 = valor_notas // 20
    valor_notas = n20 % 20

elif (valor_notas // 10) != 0:
    n10 = valor_notas // 10
    valor_notas = n10 % 10

elif (valor_notas // 5) != 0:
    n5 = valor_notas // 5
    valor_notas = n5 % 5

elif (valor_notas // 2) != 0:
    n2 = valor_notas // 2
    valor_notas = n2 % 2

# # # Moedas
# # m1 = valor_moedas // 1
# # valor_moedas = m1 % 1


# # m50 = valor_moedas // 50
# # valor_moedas = m50 % 50


# # m25 = valor_moedas // 25
# # valor_moedas = m25 % 25


# # m10 = valor_moedas // 10
# # valor_moedas = m10 % 10

# # m5 = valor_moedas // 5
# # valor_moedas = m5 % 5

# # m01 = valor_moedas // 1
# # valor_moedas = m01 % 1

print('NOTAS:')
print(f'{n100} nota(s) de R$ 100.00')
print(f'{n50} nota(s) de R$ 50.00')
print(f'{n20} nota(s) de R$ 20.00')
print(f'{n10} nota(s) de R$ 10.00')
print(f'{n5} nota(s) de R$ 5.00')
print(f'{n2} nota(s) de R$ 2.00')

# print('MOEDAS:')
# print(f'{m1} moeda(s) de R$ 1.00')
# print(f'{m50} moeda(s) de R$ 0.50')
# print(f'{m25} moeda(s) de R$ 0.25')
# print(f'{m10} moeda(s) de R$ 0.10')
# print(f'{m5} moeda(s) de R$ 0.05')
# print(f'{m01} moeda(s) de R$ 0.01')