from click import clear
import art
from game_data import data
from random import choice


print(art.logo)

def random_data():
    """Random data"""
    return choice(data)

def compare():
    count = 0
    def compare_A_B(a,b):
        if a['follower_count'] > b['follower_count']:
            return 'A'
        else:
            return 'B'

    a = random_data()
    print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}")
    print(art.vs)
    b = random_data()
    print(f"Compare B: {b['name']}, a {b['description']}, from {b['country']}")
    answer = input("Who has more followers? Type 'A' or 'B': ")

    if answer.lower() == compare_A_B(a,b).lower():
        count += 1
        clear()
    else:
        print(f"Sorry, that's wrong. Final score: {count}")
        return

    while True:
        print(art.logo)
        print(f"You're right! Current score: {count}")
        a = b
        print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}")
        print(art.vs)
        b = random_data()
        print(f"Compare B: {b['name']}, a {b['description']}, from {b['country']}")
        answer = input("Who has more followers? Type 'A' or 'B': ")

        if answer.lower() == compare_A_B(a,b).lower():
            count += 1
            clear()

        else:
            print(f"Sorry, that's wrong. Final score: {count}")
            return
compare()