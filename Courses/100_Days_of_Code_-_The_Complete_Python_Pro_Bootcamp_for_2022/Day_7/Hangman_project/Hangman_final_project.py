import random, hangman_art, hangman_words

end_of_game = False
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)
lives = 6
display = []

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
for _ in range(word_length):
    display += "_"


# while "_" in display: # enquanto houver _ em display
#   guess = input("Guess a letter: ").lower()
  
#   #Check guessed letter
#   for position in range(word_length):
#       letter = chosen_word[position]
#       #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
#       if letter == guess:
#           display[position] = letter # substitui os _ por letras
  
#   print(display)
# if "_" not in display:
#   print("You Won")


while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        
        if letter == guess:
            display[position] = letter
    
    if guess not in chosen_word:
      lives -= 1
      if lives == 0:
        end_of_game = True
        print("You lose")
    
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(hangman_art.stages[lives]) # note que os stages começam do fim, para o começo. porque nossas vidas vão diminuindo