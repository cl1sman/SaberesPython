# num1, num2 = input().split()
# num1, num2 = int(num1), int(num2)

# soma = num1 + num2

# # def zero(n):
# #     for i in n:


# def inverter(n):
#     resto = 0
#     while n > 9:
#         ultimodigito = n % 10
        
#         if ultimodigito != 0:
#             resto += ultimodigito
#             resto *= 10
#             n //= 10
#         else:
#             n //= 10
#     return (resto + n)
    

# valorinvertido1 = valornormal1 = 0
while(True):
    num1, num2 = input().split()
    num1, num2 = int(num1), int(num2)
    
    if num1 == 0 and num2 == 0:
        break

    else:
        soma = num1 + num2
        valornormal1 = int(str(soma).replace('0',''))
        print(valornormal1)


"""
def inverter(n):
    resto = 0
    while n > 9:
        ultimodigito = n % 10
        
        if ultimodigito != 0:
            resto += ultimodigito
            resto *= 10
            n //= 10
        else:
            n //= 10
    return (resto + n)


while (True):
    num1, num2 = input().split()
    num1, num2 = int(num1), int(num2)
    
    if num1 == 0 and num2 == 0:
        break

    elif num1 and num2 != 0:
        valorinvertido1 = valornormal1 = 0
        soma = num1 + num2
        valorinvertido1 = inverter(soma)
        valornormal1 = inverter(valorinvertido1)
        print(valornormal1)
"""