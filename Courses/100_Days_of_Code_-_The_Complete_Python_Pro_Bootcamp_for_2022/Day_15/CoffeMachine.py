# Imports
import os
import time
from menu import MENU, resources
from art import logo, off

# var's
money = 0
resources = resources

# functions
def report():
    global money
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")

def check_resources(order):
    """Check the resoucers"""

    if order == 'espresso' and resources['water'] >= 50 and resources['coffee'] >= 18:
        return True

    elif order == 'latte' and resources['water'] >= 200 and resources['milk'] >= 150 and resources['coffee'] >= 24:
        return True

    elif order == 'cappuccino' and resources['water'] >= 250 and resources['milk'] >= 100 and resources['coffee'] >= 24:
        return True

    else:
        print(f"Sorry there is not enough resources.")
        return False

def cost(order, coins):
    """Calculate the cost. Return the change"""
    global money
    coins[0] = coins[0] * 0.25 # quarters
    coins[1] = coins[1] * 0.10 # dimes
    coins[2] = coins[2] * 0.05 # nickles
    coins[3] = coins[3] * 0.01 # pennies
    sum_coins = sum(coins)

    if MENU[order]['cost'] <= sum_coins:
        if sum_coins > MENU[order]['cost']:
            money += MENU[order]['cost'] # add caixa
            change = round(sum_coins - MENU[order]['cost'], 2) # return change
            print(f"Here is ${change} in change.")
            return True
    else:
        print("Sorry that's not enough money. Money refunded.")

def make_the_order(order):
    """Make the order"""

    if order == 'espresso':
        resources['water'] -= MENU['espresso']['ingredients']['water']
        resources['coffee'] -= MENU['espresso']['ingredients']['coffee']
        print(f"Here is your {order} ☕️. Enjoy!")

    elif order == 'latte':
        resources['water'] -= MENU['latte']['ingredients']['water']
        resources['milk'] -= MENU['latte']['ingredients']['milk']
        resources['coffee'] -= MENU['latte']['ingredients']['coffee']
        print(f"Here is your {order} ☕️. Enjoy!")
    else:
        resources['water'] -= MENU['cappuccino']['ingredients']['water']
        resources['milk'] -= MENU['cappuccino']['ingredients']['milk']
        resources['coffee'] -= MENU['cappuccino']['ingredients']['coffee']
        print(f"Here is your {order} ☕️. Enjoy!")

# program
machine_on = True
while machine_on:
    print(logo)
    cliente_order = input("What would you like? (espresso/latte/cappuccino):")
    if cliente_order == "espresso" or cliente_order == 'latte' or cliente_order == 'cappuccino' or cliente_order == 'report':
        if cliente_order == 'report':
            report()
            time.sleep(2)
            os.system('clear')

        else:
            if check_resources(cliente_order):
                print("Please insert coins.")
                quarters = int(input("how many quarters?: "))
                dimes = int(input("how many dimes?: "))
                nickles = int(input("how many nickles?: "))
                pennies = int(input("how many pennies?: "))
                total_coins = [quarters, dimes, nickles, pennies]
                if cost(cliente_order, total_coins):
                    make_the_order(cliente_order)
                    time.sleep(2)
                    os.system('clear')
    elif cliente_order == 'off':
        print('Turning off coffee machine')
        time.sleep(2)
        print(off)
        machine_on = False
    else:
        print(f'Input invalid! Try again.')