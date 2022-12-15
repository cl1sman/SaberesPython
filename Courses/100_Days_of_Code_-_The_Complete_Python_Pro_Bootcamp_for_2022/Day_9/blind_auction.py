import os

continueWhileYes = True
bids = {}
while continueWhileYes:
    name = input('What is your name? ')
    valor = float(input('What\'s your bid?:$ '))
    bids[name] = valor
    question = input('Are there any other bidders? Type \'yes\' or \'no\'\n')
    if question == 'no':
        continueWhileYes = False
    os.system('clear')
print('The great lance is ' + max(bids) + ': $' + str(bids[max(bids)]))