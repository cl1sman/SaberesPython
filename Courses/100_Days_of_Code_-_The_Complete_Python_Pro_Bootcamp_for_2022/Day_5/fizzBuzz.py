"""
Print the number if is not divisible by 3, 5.
If is, take another print
Divisible by 3 print Fizz
Divisible by 5 print Buzz
Divisible by 3 and 5 print FizzBuzz
"""

 # 1 to 100
for _ in range(1, 101):
    if _ % 3 == 0 and _ % 5 == 0:
        print("FizzBuzz")
    elif _ % 3 == 0:
        print("Fizz")
    elif _ % 5 == 0:
        print("Buzz")
    else:
        print(_)

"""
Coloquei como primeira condição ser divisivel tanto por 3 como por 5. Porque se deixasse
para ser testado no fim, nunca seria executado, porque um número que é divisivel por 3 e
5, necessariamente será divisivel ou por 3, ou por 5.
Assim, como primeira condição, quando não for satisfeito, vai testar se é divisivel por 3
ou se é por 5.
Caso não for nenhum, será mostrado na tela o número.
"""