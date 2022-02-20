# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# weight_as_int = int(weight)
# height_as_float = float(height)

bmi = int(int(weight) / float(height) ** 2)

# bmi_as_int = int(bmi)

print(bmi)