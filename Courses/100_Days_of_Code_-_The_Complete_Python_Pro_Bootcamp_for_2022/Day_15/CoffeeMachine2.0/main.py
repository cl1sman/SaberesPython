from machine import resources, MENU

# var
caixa = 0
working_on = True

# functions
def check_resources(order):
    if order == 'espresso' and resources['water'] >= MENU['espresso']['ingredients']['water'] and resources['coffee'] >= MENU['espresso']['ingredients']['coffee']:
        return True
    elif order == 'latte' and resources['water'] >= MENU['latte']['ingredients']['water'] and resources['milk'] >= MENU['latte']['ingredients']['milk'] and resources['coffee'] >= MENU['latte']['ingredients']['coffee']:
        return True
    elif order == 'cappuccino' and resources['water'] >= MENU['cappuccino']['ingredients']['water'] and resources['milk'] >= MENU['cappuccino']['ingredients']['milk'] and resources['coffee'] >= MENU['cappuccino']['ingredients']['coffee']:
        return True
    else:
        print(f"Sorry there is not enough resources.")
        return False
def check_coins(coins, order):
    coins[0] += coins[0] * 0.25
    coins[1] += coins[1] * 0.10
    coins[2] += coins[2] * 0.05
    coins[3] += coins[3] * 0.01
    sum_coins = sum(coins)
    if sum_coins >= MENU[order]['cost']:
        return True
    else:
        print(f"Sorry that's not enough money. Money refunded.")
        return False

def payment(pay):
    global caixa
    caixa += sum(pay)

def make_order(order, coins):
    if order == "espresso":
        resources['water'] -= MENU['espresso']['ingredients']['water']
        resources['coffee'] -= MENU['espresso']['ingredients']['coffee']
        payment(coins)

    elif order == 'latte':
        resources['water'] -= MENU['latte']['ingredients']['water']
        resources['milk'] -= MENU['latte']['ingredients']['milk']
        resources['coffee'] -= MENU['latte']['ingredients']['coffee']
        payment(coins)

    elif order == 'cappuccino':
        resources['water'] -= MENU['cappuccino']['ingredients']['water']
        resources['milk'] -= MENU['cappuccino']['ingredients']['milk']
        resources['coffee'] -= MENU['cappuccino']['ingredients']['coffee']
        payment(coins)

while working_on:
    cliente_order = input("What would you like? (espresso/latte/cappuccino):")
    if check_resources(cliente_order):
        print("Please insert coins.")
        quarters = int(input("how many quarters?: "))
        dimes = int(input("how many dimes?: "))
        nickles = int(input("how many nickles?: "))
        pennies = int(input("how many pennies?: "))
        total_coins = [quarters, dimes, nickles, pennies]
        if check_coins(total_coins, cliente_order):
            make_order(cliente_order, total_coins)
    else:
        working_on = False