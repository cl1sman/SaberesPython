# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name1_lower = name1.lower()
name2_lower = name2.lower()

word_true = 0
word_love = 0

test_name = name1_lower + name2_lower

word_true += test_name.count("t")
word_true += test_name.count("r")
word_true += test_name.count("u")
word_true += test_name.count("e")

word_love += test_name.count("l")
word_love += test_name.count("o")
word_love += test_name.count("v")
word_love += test_name.count("e")

total = int(str(word_true) + str(word_love))

if total < 10 or total > 90:
    print(f"Your score is {total}, you go together like coke and mentos.")
elif total >= 40 and total <= 50:
    print(f"Your score is {total}, you are alright together.")
else:
    print(f"You score is {total}")