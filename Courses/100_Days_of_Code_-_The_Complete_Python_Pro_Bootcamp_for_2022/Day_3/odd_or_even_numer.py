# 🚨 Don't change the code below 👇
from math import remainder


number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

remainder = number % 2

if remainder == 0: # or if number % 2 == 0: (excluindo a necessidade da variavel remainder)
    print("This is an even number")
else:
    print("This is an odd number")