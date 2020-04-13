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

#######################################


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
