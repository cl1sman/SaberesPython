# Aprendendo a usar funções

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