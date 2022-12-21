# Add
def add(n1, n2):
    return n1 + n2


# Subtract
def subtract(n1, n2):
    return n1 - n2


# Mult
def multiply(n1, n2):
    return n1 * n2


# Divide
def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

num1 = int(input('First numer: '))

for key in operations:
    print(key)

operations_symbol = input('Choose operatioins symbol: ')
num2 = int(input('Second number: '))

calculation_function = operations[operations_symbol]  # ex: add, aqui escolho 'value'
answer = calculation_function(num1, num2)  # ex: add(a, b), aqui passo os argumentos por parametro
print(f'{num1} {operations_symbol} {num2} = {answer}')
