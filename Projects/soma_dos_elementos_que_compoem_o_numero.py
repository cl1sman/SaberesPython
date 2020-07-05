# Digite um numero inteiro, e a soma dos elementos que compoem este numero serao somados.
x = int(input('Number: '))
y = 0
sum = 0

while x != 0:
    y = x % 10 # ultimo numero
    x = x // 10 # elimina o ultimo numero
    sum = sum + y

print('Soma do numero: ',sum)