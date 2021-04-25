num1 = int(input('Número 1: '))
num2 = int(input('Número 2: '))
num3 = int(input('Número 3: '))

# crescente
if num1 < num2 and num1 < num3 and num2 < num3:
    print('crescente')
else:
    print('não está em ordem crescente')