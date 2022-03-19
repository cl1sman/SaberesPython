# A forma mais eficaz para resolver um grande problema
# é dividi-lo em problemas menores.
# Assim, dividir um grande problema em pequenas partes.
# Não tente resolver tudo de uma vez, tome, e o divida em partes menores

#Step 1 

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
import random
chosen_word = random.choice(word_list)

# Testing code
print(chosen_word)

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Guess a letter: ").lower()

display = []
word_length = len(chosen_word)
# using range for this. blank letters
for _ in range(word_length):
  display.append("_")

# their match?
for i in range(word_length):
    if chosen_word[i] == guess:
        display[i] = guess
print(display)