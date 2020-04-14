# Aprendendo a usar funções


# ||    Posso fazer uma função sem passar argumentos, tendo uma função fechada

def mult_two_add_three(): # aqui, a função não tem argumentos, parametros. Então nela a variavel será number = 5 apenas. Assim,
    number = 5            # tenho uma função fechada
    print(number*2 + 3)


# Chamando a função
mult_two_add_three() # a função é chamada, porem sem parametros


# ||    Para tornar a função mais útil, posso passar argumentos, parametros para este função. Assim, ao invés de ter uma variavel
#       com um valor fixo, posso passar valor a esta função

def mult_two_add_three(number): # na função, passei como parametro a variavel number. Assim, quando chamar a função, passarei o 
    print(number*2 + 3)         # valor que quero que number assuma

mult_two_add_three(1) # neste caso, o para o parametro/argumento da função, estou passando o valor 1. Assim, nummber assumira o valor 1


#   ||    # Passando por uma variavel o valor do parametro que a função assumira
def mult(number):
    print(number*2 + 3)

x = int(input('Informe o valor: '))
mult(x)
#____________________________________________________________________________________________________________________________________#

#   Exemplo:
def mult_x_add_y(number, x, y):
    print(number*x + y)

mult_x_add_y(5, 2, 3)

#   Exemplo:
def greet_customer(grocery_store, special_item):
    print('Welcome to ' + grocery_store + '.')
    print('Our special is ' + special_item + '.')
    print('Have fun shopping')

greet_customer('Naruto doces', 'Hakuna Matata')

#_____________________________________________________________________________________________________________________________________#

#   Exemplo:
def calculate_age(current_year, birth_year):
    age = current_year - birth_year
    return age

my_age = calculate_age(2020, 1993)

print(my_age)

#_____________________________________________________________________________________________________________________________________#

def square_point(x_value, y_value):
    x_2 = x_value * x_value
    y_2 = y_value * y_value
    return x_2, y_2
    
x_squared, y_squared = square_point(1, 3)
print(x_squared)
print(y_squared)

"""
    x_quared, y_quared = square_point(1, 3)

    a função square_point é chamada, com os valores 1 e 3. Assim, a função faz o que tem que fazer
    e retorna dois valores. Estes valores voltam na mesma sequencia. Ou seja, o primeiro resultado
    volta na posição 0, e o segundo na 1.

    Assim, x_squared que esta na primeira posição (posição 0), recebe o primeiro valor, e o segun-
    do que se encontra na posição 1 recebe o segundo valor.

    Então, a função recebe dois valores em sequencia, rertona os resultados na mesma sequencia.
    Então x_squared, y_squared recebe seus respectivos valores.
"""
#_____________________________________________________________________________________________________________________________________#
"""
    Posso passar o valor de uma variavel para a função.
    Mas não posso tentar usar uma variavel de dentro de uma função fora dela _>

    def create_special_string(special_item):
        return 'Our special is ' + special_item + '.'
    
    print('I dont like ' + special_item)

    special_item, nesta situação não pode ser usado desta forma, ocassionara em um erro NameError
    
"""
header_string = 'Our special is '

def create_special_string(special_item):
    return header_string + special_item + '.'

print(create_special_string('grapes'))

#_____________________________________________________________________________________________________________________________________#
ano_atual = int(input('Informe o ano atual: '))

def quantos_anos_tenho(ano_que_nasceu):
    idade = ano_atual - ano_que_nasceu
    return idade

ano_informado = int(input('Informe o ano em que nasceu: '))

print('Você tem ' + str(quantos_anos_tenho(ano_informado)) + ' anos de idade')

#_____________________________________________________________________________________________________________________________________#
# Exemplo com argumento padrão

def repeat_stuff(stuff, num_repeats = 10):
  return(stuff*num_repeats)

lyrics = repeat_stuff('Row ', 3) + 'Your Boat. '
song = repeat_stuff(lyrics) # o argumento será lyrics, porque num_repeats esta default = 10, então stuff recebe lyrics
print(song)                 # e o num_repeats = 10. E necessario ser nesta sequencia, se stuff tivesse um valor default
                            # seria problema, porque os parametros são passados na sequencia. Assim, se tivesse stuff 
                            # um parametro padrão daria erro, pois o segundo num_repeats não teria um valor atribuido
                            # SyntaxError: non-default argument follows default argument
                            # Para que não ocorra este erro, devo deixar padrão um valor, contanto que ao informar o
                            # outro, este seja passado na sequencia certa.
                            # No caso aqui, ao deixar o segundo parametro padrão, ao ser chamado a segunda vez, terá
                            # 10 atribuido como padrão, faltando somente o primeiro argumento.
#_____________________________________________________________________________________________________________________________________#
# Funções para aula de Fisica
train_mass = 22680
train_acceleration = 10
train_distance = 100

bomb_mass = 1



# function for fahrenheit to celsius
def f_to_c(f_temp):
  c_temp = (f_temp -32) * 5/9
  return c_temp

f100_in_celsius = f_to_c(100)



# function celsius to fahrenheit
def c_to_f(c_temp):
  f_temp = c_temp * (9/5) + 32
  return f_temp

c0_in_fahrenheit = c_to_f(0)



# function for Force
def get_force(mass, acceleration):
  return mass*acceleration

train_force = get_force(train_mass, train_acceleration)
print(train_force)
print('The GE train supplies '+ str(train_force) + 'Newtons of force ')



def get_energy(mass, c=3*10**8):
  return mass*c
bomb_energy = get_energy(bomb_mass)
print('A 1kg bomb supplies ' + str(bomb_energy) + ' joules')



# uma função dentro da outra. Quando a função get_work for chamada, ela vai chamr a função get_force
def get_work(mass, acceleration, distance):
  return get_force(mass, acceleration) * distance

train_work = get_work(train_mass, train_acceleration, train_distance)
print('The GE train does ' + str(train_work) + ' Joules of work over ' + str(train_distance) + ' meters')
#_____________________________________________________________________________________________________________________________________#


def get_initial(name):
    initial = name[0:1]
    return initial

first_ = input('Enter your first name: ')
first_inicial = get_initial(first_)

last_ = input('Enter your last name: ')
last_inicial = get_initial(last_)

print('Your initial is: ' + first_inicial + last_inicial)

# Dando opção de upper()

def get_inicial(nome, opção_uppercase):
    if opção_uppercase:
        inicial = nome[0:1].upper()
    else:
        inicial = nome[0:1]
    return inicial

primeiro_nome = input('Entre com o primeiro nome: ')
inicial_primeiro_nome = get_inicial(nome=primeiro_nome, opção_uppercase=True)

segundo_nome = input('Entre com o ultimo nome: ')
inicial_segundo_nome = get_inicial(nome=segundo_nome, opção_uppercase=True)

print('Suas iniciais são: ' + inicial_primeiro_nome + inicial_segundo_nome)
