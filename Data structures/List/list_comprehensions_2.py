usernames = ['@coolguy35', '@kewldawg54', '@matchamom']
# new list
messages = [user + ' please follow me!' for user in usernames]
print(messages)

# 1. user vai receber os elementos em sequencia de usernames, um por vez.
# 2. agora que user tem um dos elementos de usernames, será adicionado + ' please follow me!', será repetido até terminar.
# 3. é atribuido a lista messages


# other exemplo
celsius = [0, 10, 15, 32, -5, 27, 3]

# Os dados serão armazenados em uma nova lista
fahrenheit = [temperature_in_celsius * 9/5 + 32 for temperature_in_celsius in celsius]
print(fahrenheit)

# 1. temperature_in_celsius vai receber um dos valores de celsius
# 2. agora que temperature_in_celsius tem um dos valores de celsius, o calculo será feito. 
# Ou seja, temperature_in_celsius * 9/5 + 32 será executado.

##############################################################################################################################
single_digits = range(0,10)

squares = []

for s_d in single_digits:
  squares.append(s_d**2)
  print(s_d)
print(squares)

cubes = [single**3 for single in single_digits]
print(cubes)

# Others
my_list = [5, 10, -2, 8, 20]
desired_list = [i for i in my_list if i > 5]
print(desired_list)