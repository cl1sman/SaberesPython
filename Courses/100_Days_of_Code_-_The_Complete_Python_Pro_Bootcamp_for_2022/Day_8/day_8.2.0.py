#Write your code below this line 👇
def prime_checker(number):
    cont = 0
    for i in range(1, number+1):
        if number % i == 0 and number % 1 == 0:
            cont += 1
    if cont == 2:
        return print(f"{number} is a prime number")
    else:
        return print(f"{number} is not a prime number")





#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)