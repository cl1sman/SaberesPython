print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")

    age = int(input("What is your age? "))
    # apenas uma das três condições abaixo será satisfeita.
    if age < 12:
        bill = 5
        print("Childe tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    else:
        bill = 12
        print("Adult tickets are $12.")
    
    # após uma das três condições ser satisfeita. Esta pergunta será feita. 
    # Desta forma, não importa qual condição, vai passar pela proxima
    wants_photo = (input("Do you want a photo taken? Y or N."))
    if wants_photo.upper() == "Y": # caso a entrada seja em letra miniscula, o "method" .upper() ira deixar a "string" maiuscula (não modificando a string que esta na variavel)
        bill += 3
    
    print(f"Your final bill is ${bill}")
else:
    print("Sorry, you have to grow taller before you can ride.")