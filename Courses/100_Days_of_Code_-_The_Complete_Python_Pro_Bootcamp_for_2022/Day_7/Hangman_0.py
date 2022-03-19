import random
# Gerate a random word
words = ["coelho", "bode", "pera", "baleia", "arvore"]
word = random.choice(words)

# generate as many blanks as letters in word
blacks_letters = len(word) * "_"

game_over = False
while game_over != True:
    guess_letter = input("Letter: ")

    if guess_letter in word:
        # replace the blank with the letter
        print()