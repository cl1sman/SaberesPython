"""Cards Jack, Queen and King = 10. Ace is 1, or 11 (depend if you've gone over 21, or whether if you're under 21, your can decide). The numbers has the number represent. Max 21, if you pass, your lose"""
from random import choices


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] # Ace 1 or 11. Numbers 2-10. Jack, Queen and King = 10

def deal_card():
    return choices(cards) # k is the length of the returned list
def calculate_score(a):
    score = 0
    for i in a:
        score += sum(i)
    # Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game
    # check blackjack
    if len(a) == 2:
        if score == 21:
            return 0 # zero represents a blackjack
    return score

user_cards = []
computer_cards = []
# Start with 2 cards
user_cards.append(deal_card())
user_cards.append(deal_card())
computer_cards.append(deal_card())
computer_cards.append(deal_card())

print(f'User cards score {calculate_score(user_cards)}')
print(f'Computer cards score {calculate_score(computer_cards)}')

