import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇

"""
  Roles for Rock, Paper and Scissors
  * Rock wind against scissors
  * Scissors win against paper
  * Paper wins against rock
"""


images = [rock, paper, scissors]

chose = int(input("Whaat do you chose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))

if chose >= 3 or chose < 0:
    print("You typed an invalid number, you lose!")
else:

    print(images[chose])

    # ambos os limites estão inclusos. Tando o inicio como o fim
    computer_chose = random.randint(0, 2)
    print("Computer chose")
    print(images[computer_chose])

    """
    As combinações que encontrei:
    0-2  2-0
    0-1  1-0
    1-2  2-1
    2-0  0-2
    """

    # 0-2 2-0
    if chose == 0 and computer_chose == 2:
        print("You win")
    elif chose == 2 and computer_chose == 0:
        print("You lose")

    # """
    #   Lembre-se, aqui será satisfeita apenas uma opção. Não é multi-if. Ou seja, se um if for satisfeito, o programa não
    #   ira continuar testando o restante. Pois se encontrar um if que o satisfaça, ele ira o executar.

    #   Desta forma, se passou pelos testes anteriores e não foram satisfeitos, não será feito novamente.

    #   As condições anteriores tratam das comparações entre 2 e 0, e 0 e 2. Logo, se chegou até aqui, é obvio que não será uma
    #   comparação entre 2 e 0 ou 0 e 2, porque se fossem, não teriam chegado até aqui. Logo, trato de opções diferentes.
    # """

    elif chose > computer_chose:
        print("You win")
    elif chose < computer_chose:
        print("You lose")
    elif chose == computer_chose:
        print("It's a draw")