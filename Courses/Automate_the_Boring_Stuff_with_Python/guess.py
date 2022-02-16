# This is a guess the number game.
import random

print('Hello. What is your name?')
name = input()

print(f'Well, {name}, I am thinking of a number between 1 and 20.')
secretNumber = random.randint(1, 20) # random int. [1, 20], inclui 1 e o 20

# print(f'DEBUG: Secret number is {str(secretNumber)}')

for guessesTaken in range(1, 7): # range(6). Starting at zero and going up to but not including six. range(1, 7), start 1, and not including 7
    print('Take a guess.')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break # This condition is for the correct guess!

if guess == secretNumber:
    print(f'Good job, {name}! You guessed my number in {str(guessesTaken)} guess!')
else:
    print(f'Nope. The number I was thinking of was {str(secretNumber)}')

print(f'You took {str(guessesTaken)} guesses.') # posso usar guessesTaken, porque ele vai ser o contador aqui, guardando o valor de range, de [0,6[
