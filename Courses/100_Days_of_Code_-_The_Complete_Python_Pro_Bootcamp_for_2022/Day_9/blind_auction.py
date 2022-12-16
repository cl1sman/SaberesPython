import os

continueWhileYes = True
bids = {}
while continueWhileYes:
    name = input('What is your name?\n')
    valor = float(input('What\'s your bid?:\n$'))
    bids[name] = valor
    question = input('Are there any other bidders? Type \'yes\' or \'no\'\n')
    if question.lower() == 'no':
        continueWhileYes = False
    os.system('clear')
# greater = 0
# for i in bids:
#     if bids[i] > greater:
#         greater = bids[i]
#         win = i
# print('Greater bids ' + win + ' $' + str(greater))

# other way, no need comparation
# max_value = max(bids.values()) # value
# max_key = max(bids, key=bids.get) # key
# print(f'The greater is {max_key}: ${max_value}')
for i in bids:
    print(f'{i}: {bids[i]}')
print(f'The highest bidder was {max(bids, key=bids.get)}: ${max(bids.values())}')