#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
from art import logo
from random import randint
def randomNumber():
	"""Choose randomic number between 1 to 100"""
	return randint(1, 100)
def playGame():
	print(logo)
	print("Welcome to the Number Guessing Game!")
	print("I'm thinking of a number between 1 and 100.")
	number = randomNumber()
	chooseDificultGame = input("Choose a difficulty. Type 'easy' or 'hard':")
	if chooseDificultGame == 'easy':
		modeGame = 10
		print("You have 10 attempts remaining to guess the number.")
	elif chooseDificultGame == 'hard':
		modeGame = 5
		print("You have 5 attempts remaining to guess the number.")
	
	attempts = modeGame
	for _ in range(modeGame):
		attempts -= 1
		myGuess = int(input("Make a Guess: "))
		if myGuess is not number:
			if myGuess < number:
				print("Too low.")
				print("Guess again.")
				print(f"You have {attempts} attempts remaining to guess the number.")				
			elif myGuess > number:
				print("Too high.")
				print("Guess again.")
				print(f"You have {attempts} attempts remaining to guess the number.")
			

		elif myGuess is number:
			return f"You got it! The answer was {number}."
	print("You've run out of guesses, you lose.")
playGame()				