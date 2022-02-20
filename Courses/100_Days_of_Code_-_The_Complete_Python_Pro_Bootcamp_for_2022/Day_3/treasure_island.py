print("Welcome to Treasure Island.\nYout mission is to find treasure.")
question = input("Left or Right? ")
if question.lower() == "right":
    print("Fall into a hole.\nGame Over.")
else:
    question = input("swim or wait? ")
    if question.lower() == "swim":
        print("Attacked by trout.\nGame Over.")
    else:
        question = input("Which door? Red, Blue or Yellow?")
        if question.lower() == "red":
            print("Burned by fire.\nGame Over.")
        elif question.lower() == "blue":
            print("Eaten by beasts.\nGame Over.")
        else:
            print("You Win!")