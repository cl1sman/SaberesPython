#Write your code below this line 👇
def prime_checker(number):
    prime = True
    for i in range(2, number): # every number is divided by 1
        if number % i == 0: # if the number is divided by any number other than 1 and ifself, it is not a prime number
            prime = False
    if prime:
        return print(f"{number} is a prime number")
    else:
        return print(f"{number} is not a prime number")




#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)